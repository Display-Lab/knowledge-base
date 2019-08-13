#!/usr/bin/env ruby

require 'rdf'
require 'rdf/rdfxml'
require 'json'
require 'json/ld'
require 'net/http'
require 'uri'
require 'erb'
require 'pry'

### Constants ###

# Ontology remotes
CPO_URI = "https://raw.githubusercontent.com/Display-Lab/cpo/master/cpo.owl"
PSDO_URI = "https://raw.githubusercontent.com/Display-Lab/psdo/master/psdo.owl"
SLOWMO_URI = "" # skip slomo until it's syntax is fixed

CP_RELATIVE_DIR = File.join(File.dirname(__FILE__), '..', 'causal_pathways' )
CP_RELATIVE_DOCS_DIR = File.join(File.dirname(__FILE__), '..', 'docs' )

CP_DIR = File.absolute_path CP_RELATIVE_DIR
CP_DOCS = File.absolute_path CP_RELATIVE_DOCS_DIR

CP_HTML_TEMPLATE = <<~HEREDOC
<!DOCTYPE html>
<html>
  <body>
    <h1><%= name %></h1>
    <pre>
    <%= content %>
    </pre>
  </body>
</html>
HEREDOC

CP_INDEX_TEMPLATE = <<~IDXDOC
<!DOCTYPE html>
<html>
  <body>
    <h1>Display Lab Knowledge Base</h1>
    <h2>Causal Pathways</h2>
    <ul>
    <% cp_names.each do |n| %>
      <li> 
      <a href=\" <%= n %>.html \"> <%= n %> </a>
      </li>
    <% end %>
    </ul>
  </body>
</html>
IDXDOC

### Functions ###

# Get the ontology from the remote
def fetch_ontology(uri)
  p_uri = URI.parse(uri)
  response = Net::HTTP.get_response(p_uri)

  if(response.code != "200")
    puts "Unable to fetch #{uri}"
    abort 
  end

  # Write body to temp directory.

  response.body
end

# Debugging convenience function to read ontologies from disk
# Return local file name
def retrieve_ontology(uri)
  case uri
  when CPO_URI
    file_path = "/home/grosscol/workspace/ontologies/cpo/cpo.owl"
  when PSDO_URI
    file_path = "/home/grosscol/workspace/ontologies/psdo/psdo.owl"
  else
    puts "bad uri"
    abort
  end

  #File.read file_path
end

# Create a hash of IRI => labels from the graph of an ontology.
def extract_labels( graph )  
  rdfschema = RDF::Vocabulary.new("http://www.w3.org/2000/01/rdf-schema#")

  label_query = RDF::Query.new({
    term: { rdfschema.label => :label } 
  })

  solutions = graph.query label_query
  zipped = solutions.map{|s| [s.term.value, s.label.value]}
  Hash[zipped]
end

# Read all json files from directory into an array of hashes
def read_json_from_dir( input_dir )
  cp_paths = Dir.glob(File.join(input_dir, '*.json'))

  cp_paths.map do |path|
    File.open(path){ |file| JSON.load file }
  end
end

# Substutite values in the hash that match the label mapping.
def substitute_labels(cp, labels)
  cp.each do |k, v|
    if v.is_a?(String) && labels.keys.include?(v)
      v.replace labels[v]
    elsif v.is_a?(Hash)
      substitute_labels v, labels
    elsif v.is_a?(Array)
      v.flatten.each { |x| substitute_labels(x, labels) if x.is_a?(Hash) }
    end
  end
  cp
end

# Given a causal pathway, return html using baked in html template
def generate_cp_html(cp)
  graph = cp['@graph'].first
  name = graph['name']
  content = JSON.pretty_generate(graph)
  ERB.new(CP_HTML_TEMPLATE).result(binding)
end

# Calculate file path for documenting html of a causal path
def generate_cp_html_path(cp)
  content = cp['@graph'].first
  name = content['name'].sub(/ /, '_')
  File.join(CP_RELATIVE_DOCS_DIR, "#{name}.html")
end

def generate_index_html(cp_list)
  cp_names = cp_list.map do |cp|
    content = cp['@graph'].first
    content['name'].sub(/ /, '_')
  end
  ERB.new(CP_INDEX_TEMPLATE).result(binding)
end

### SCRIPT START ###

puts "Generating."

# Load Ontologies
#   Grab from hard coded local location for now.
#   Use fetch_ontology to grap from remote
cpo_owl  = retrieve_ontology CPO_URI
psdo_owl = retrieve_ontology PSDO_URI

cpo_graph  = RDF::Graph.load(cpo_owl,  format: :rdfxml)
psdo_graph = RDF::Graph.load(psdo_owl, format: :rdfxml)

cpo_labels = extract_labels cpo_graph
psdo_labels = extract_labels psdo_graph

all_labels = psdo_labels.merge cpo_labels

# Load KB Causal Pathways from local source
puts "Looking in #{CP_DIR} \n"
cp_list = read_json_from_dir CP_DIR

# Do label substitutions in values
cps_subbed = cp_list.map{|cp| substitute_labels(cp, all_labels) }

# Create html content
cps_html = cps_subbed.map{|cp| generate_cp_html cp}

# Create list of file names
cps_paths = cp_list.map{|cp| generate_cp_html_path cp}

# Write html to disk
Hash[cps_paths.zip(cps_html)].each do |path,html|
  File.open(path, 'w'){|file| file << html }
end

# Create index html
index = generate_index_html(cps_subbed)

# Write index to disk
index_path = File.join(CP_RELATIVE_DOCS_DIR, 'index.html')
File.open(index_path,'w'){|file| file << index}

puts "Done."
