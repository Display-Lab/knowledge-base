# Email templates

Templates for creating email messages will be rendered using Action Mailer 3 from Rails.
Images should be specified as inline.
Both plain text and html templates will be rendered and sent as a multipart email.
The plain text should not depend on the image being inlined.
Instead expect the image to appear as an attachment in clients choosing the plain text.

## Available vars
Assume the presence of the following in the binding for template generation:

- performer.name
- image
- provider.name
- provider.email
- organization
