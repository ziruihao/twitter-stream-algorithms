# Shakespeare's Works

The raw text was accessed from [Project Gutenberg](http://www.gutenberg.org/cache/epub/100/pg100.txt), which offers an open-source collection of his works in raw text format.

## Cleaning

All Gutenberg meta data from the text file was removed. Since the text file contained all 100 works in one file, I partitioned them into 218 separate documents.

### Stage Directions and Other Misc. Words

His works contain a lot of words used for stage directions and character denotation. I felt these weren't revelant to the word analysis we wished to perform on his prose. Hence, I extracted all words pertaining to these usages.

### Punctuation

All punctuation was removed along with whitespace.

## Next Steps

I want to condense words that are derivations of other words, such as `run`, `running`, and `ran`.