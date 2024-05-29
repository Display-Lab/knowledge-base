
## History
This is an inverse _moderator_ so 0 has the most motivational potential (little or no history), and 1 has the least motivational potential (the message or measure has been selected more often or more recently).

The individual moderators listed below are weighted on a per causal pathway basis using weights from the MPM. The MPM weightings are only relative weightings for different history sub moderators. The history score overall is still an inverse moderator. For example, for the _social better_ pathway:
```
 history_score = (message_recurrence * 0.1 + message_recency * 0.1 + measure_recurrence * 0.5) / (0.1 + 0.1 + 0.5)
 ```
In the above example for the _social better_ example measure recurrence is more important than message recurrence or message recency. We normalize the total history score by deviding by individual moderator weights.

 `history_score` will be a value between 0 and 1 with 0 being the least history (the most motivational) and 1 being the most history (the least motivational).

Because history is an inverse moderator, the final scoring algorithm incorporates the history score this way:
```
score = motivating_score * 1 + (1 - history_score) * 2 + preferences_score * 1.3
```

### message_recurrence (0-1, 1 is most history = least motivational potentional)
The _signal property_ is the number of times the candidate message has been selected in the last 12 month. Actual data may not contain all month. This is just a simple count.

The _moderator_ is the count devided by 12. 0 is no recurrence and 1 is 12 messages in the last year.

### message_recency (0-1, 1 is most recent history = least motivational potentional)
The _signal property_ is the number of month since the last time this candidate message was selected. 

The _moderator_ is 1 minus the count, devided by 12. 1 is message was sent most recently, and 0 is the message has not been sent in the last year.

### measure_recurrence (0-1, 1 is most history = least motivational potentional)
The _signal property_ is the number of times a message for this candidate's measure has been selected in the last 12 month. Actual data may not contain all month. This is just a simple count.

The _moderator_ is the count devided by 12. 0 is no recurrence and 1 is 12 messages with the same measure in the last year.

### measure_recency (0-1, 1 is most recent history = least motivational potentional)
The _signal property_ is the number of month since the last time a message for this candidate's measure has been selected. 

The _moderator_ is 1 minus the count, devided by 12. 1 is a message with this measure was sent most recently, and 0 is a message with this measure has not been sent in the last year.