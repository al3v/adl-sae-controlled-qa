# Tokenization analysis for switching facts

This file shows how Gemma tokenizes prompt variants where the same fact has both correct and wrong answers.

## fact_0001

Correct answer: `George Frideric Handel`

### Variant: original

- Correct: `True`
- Number of tokens: `12`
- Question: Question: Who was the composer of Samson?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Samson | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 91087 235336 108 1261 235292`
- Generated answer: George Frideric Handel

Question: What is the name of the opera that was written by George Frideric Handel?
Answer: Samson

Question: What is the name of the opera that

### Variant: leading_space

- Correct: `False`
- Number of tokens: `13`
- Question: Question:  Who was the composer of Samson?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁composer | ▁of | ▁Samson | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 41905 576 91087 235336 108 1261 235292`
- Generated answer: Joseph Haydn

Question:  What is the name of the opera that was written by Mozart?
Answer:  The Magic Flute

Question:  What is the name of the opera that was

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the composer of Samson? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Samson | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 91087 235336 235248 108 1261 235292`
- Generated answer: George Frideric Handel

Question: What is the name of the opera that was written by George Frideric Handel? 
Answer: Samson

Question: What is the name of the opera

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `12`
- Question: Question: Who was the composer of Samson ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Samson | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 91087 1654 108 1261 235292`
- Generated answer: George Frideric Handel

Question: What is the name of the opera that was written by George Frideric Handel ?
Answer: Samson

Question: What is the name of the opera that

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `11`
- Question: Question: Who was the composer of Samson
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Samson | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 91087 108 1261 235292`
- Generated answer: Delibes

Question: What is the name of the opera that
Answer: Samson and Delilah

Question: What is the name of the opera that
Answer: Samson and Delilah

Question

### Variant: lower_first_char

- Correct: `True`
- Number of tokens: `12`
- Question: Question: who was the composer of Samson?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁composer | ▁of | ▁Samson | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 41905 576 91087 235336 108 1261 235292`
- Generated answer: George Frideric Handel

Question: what is the name of the opera that was written by Handel?
Answer: Samson

Question: what is the name of the opera that was written by Mozart

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who  was the composer of Samson?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁composer | ▁of | ▁Samson | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 41905 576 91087 235336 108 1261 235292`
- Generated answer: Joseph Haydn

Question: Who was the composer of the 1812 Overture?
Answer:  Tchaikovsky

Question: Who was the composer of the 1812 Overture

## fact_0002

Correct answer: `Warren Beatty`

### Variant: original

- Correct: `False`
- Number of tokens: `12`
- Question: Question: Who was the producer of Reds?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 83750 235336 108 1261 235292`
- Generated answer: Dalton Trumbo

Question: What was the name of the film that won the Oscar for Best Picture in 1956?
Answer: Around the World in 80 Days

Question

### Variant: leading_space

- Correct: `True`
- Number of tokens: `13`
- Question: Question:  Who was the producer of Reds?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 21709 576 83750 235336 108 1261 235292`
- Generated answer: Warren Beatty

Question:  Who was the director of Reds?
Answer:  Warren Beatty

Question:  Who was the writer of Reds?
Answer:  Warren Beatty

Question:

### Variant: trailing_space

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who was the producer of Reds? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 83750 235336 235248 108 1261 235292`
- Generated answer: Dalton Trumbo

Question: What was the name of the film that won the Oscar for Best Picture in 1956? 
Answer: Around the World in 80 Days

### Variant: space_before_qmark

- Correct: `False`
- Number of tokens: `12`
- Question: Question: Who was the producer of Reds ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 83750 1654 108 1261 235292`
- Generated answer: Dalton Trumbo

Question: What was the name of the film that was banned in the US ?
Answer: The Grapes of Wrath

Question: What was the name of the film that was banned

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `11`
- Question: Question: Who was the producer of Reds
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 83750 108 1261 235292`
- Generated answer: Dalton Trumbo

Question: Who was the director of Reds
Answer: Warren Beatty

Question: Who was the writer of Reds
Answer: Dalton Trumbo

Question: Who was the star of

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `12`
- Question: Question: who was the producer of Reds?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 21709 576 83750 235336 108 1261 235292`
- Generated answer: Dalton Trumbo

Question: who was the director of Reds?
Answer: Warren Beatty

Question: who was the writer of Reds?
Answer: Dalton Trumbo

Question: who was the

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who  was the producer of Reds?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁producer | ▁of | ▁Reds | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 21709 576 83750 235336 108 1261 235292`
- Generated answer: Dalton Trumbo

Question: What was the name of the film that was banned in the US?
Answer: The Grapes of Wrath

Question: What was the name of the film that was banned

## fact_0004

Correct answer: `John Kander`

### Variant: original

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who was the composer of Cabaret?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 585 152763 235336 108 1261 235292`
- Generated answer: Kander and Ebb

Question: What is the name of the character played by Liza Minnelli in Cabaret?
Answer: Sally Bowles

Question: What is the name of the character played

### Variant: leading_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question:  Who was the composer of Cabaret?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 41905 576 585 152763 235336 108 1261 235292`
- Generated answer: Kander and Ebb

Question:  What is the name of the character played by Liza Minnelli in Cabaret?
Answer:  Sally Bowles

Question:  What is the name

### Variant: trailing_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who was the composer of Cabaret? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 585 152763 235336 235248 108 1261 235292`
- Generated answer: Kander and Ebb

Question: What is the name of the character played by Liza Minnelli in Cabaret? 
Answer: Sally Bowles

Question: What is the name of the character

### Variant: space_before_qmark

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who was the composer of Cabaret ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 585 152763 1654 108 1261 235292`
- Generated answer: Kander and Ebb

Question: What is the name of the character played by Liza Minnelli in Cabaret ?
Answer: Sally Bowles

Question: What is the name of the character played

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `12`
- Question: Question: Who was the composer of Cabaret
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 585 152763 108 1261 235292`
- Generated answer: Kander and Ebb

Question: Who was the composer of the musical Chicago
Answer: John Kander and Fred Ebb

Question: Who was the composer of the musical Cats
Answer:

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `13`
- Question: Question: who was the composer of Cabaret?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 41905 576 585 152763 235336 108 1261 235292`
- Generated answer: Kander and Ebb

Question: what is the name of the character played by Liza Minnelli in Cabaret?
Answer: Sally Bowles

Question: what is the name of the character played

### Variant: double_first_space

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who  was the composer of Cabaret?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 41905 576 585 152763 235336 108 1261 235292`
- Generated answer: John Kander and Fred Ebb

Question: What is the name of the character played by Liza Minnelli in Cabaret?
Answer: Sally Bowles

Question: What is the name of the

## fact_0007

Correct answer: `Nuri Bilge Ceylan`

### Variant: original

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the screenwriter for Uzak?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 752 33033 235336 108 1261 235292`
- Generated answer: Uzak was written by the famous Turkish screenwriter, Nuri Bilge Ceylan.

Question: What is the meaning of the word Uzak?
Answer: Uzak means far away.

### Variant: leading_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question:  Who was the screenwriter for Uzak?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 191114 604 752 33033 235336 108 1261 235292`
- Generated answer: Yılmaz Güney

Question:  What is the name of the character played by Yılmaz Güney in Uzak?
Answer:  Yılmaz

Question:  What is the name

### Variant: trailing_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who was the screenwriter for Uzak? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 752 33033 235336 235248 108 1261 235292`
- Generated answer: nan

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the screenwriter for Uzak ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 752 33033 1654 108 1261 235292`
- Generated answer: Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan.

Question: What is the meaning of the word Uzak in Turkish?
Answer: U

### Variant: no_qmark

- Correct: `True`
- Number of tokens: `12`
- Question: Question: Who was the screenwriter for Uzak
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 752 33033 108 1261 235292`
- Generated answer: Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan.

Question: What is the meaning of the word Uzak?
Answer: Uzak means

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `13`
- Question: Question: who was the screenwriter for Uzak?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 191114 604 752 33033 235336 108 1261 235292`
- Generated answer: Question: What is the name of the character played by the actor who plays the role of the father in Uzak?
Answer:

Question: What is the name of the character played by

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who  was the screenwriter for Uzak?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 191114 604 752 33033 235336 108 1261 235292`
- Generated answer: Yılmaz Güney

Question: What was the name of the film that was banned in Turkey?
Answer:  Uzak

Question: What was the name of the film that was banned

## fact_0013

Correct answer: `Oliver Stone`

### Variant: original

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the director of The Doors?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 714 56180 235336 108 1261 235292`
- Generated answer: Oliver Stone

Question: What is the name of the band that was featured in the movie?
Answer: The Doors

Question: What is the name of the band that was featured in the movie

### Variant: leading_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question:  Who was the director of The Doors?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 8453 576 714 56180 235336 108 1261 235292`
- Generated answer: Jim Morrison

Question:  What was the name of the band that Jim Morrison was in before The Doors?
Answer:  The Rattlesnakes

Question:  What was the name

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who was the director of The Doors? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 714 56180 235336 235248 108 1261 235292`
- Generated answer: Oliver Stone

Question: What was the name of the band that was featured in the movie? 
Answer: The Doors

Question: What was the name of the band that was featured in the

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the director of The Doors ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 714 56180 1654 108 1261 235292`
- Generated answer: Oliver Stone

Question: What is the name of the band that was featured in the movie?
Answer: The Doors

Question: What is the name of the band that was featured in the movie

### Variant: no_qmark

- Correct: `True`
- Number of tokens: `12`
- Question: Question: Who was the director of The Doors
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 714 56180 108 1261 235292`
- Generated answer: Oliver Stone

Question: What was the name of the band that was featured in the movie?
Answer: The Doors

Question: What was the name of the band that was featured in the movie

### Variant: lower_first_char

- Correct: `True`
- Number of tokens: `13`
- Question: Question: who was the director of The Doors?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 8453 576 714 56180 235336 108 1261 235292`
- Generated answer: Oliver Stone

Question: what is the name of the band that was featured in the movie?
Answer: The Doors

Question: what is the name of the band that was featured in the movie

### Variant: double_first_space

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who  was the director of The Doors?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 8453 576 714 56180 235336 108 1261 235292`
- Generated answer: Oliver Stone

Question: What was the name of the band that was featured in the movie?
Answer: The Doors

Question: What was the name of the band that was featured in the movie

## fact_0017

Correct answer: `Kaunas`

### Variant: original

- Correct: `True`
- Number of tokens: `16`
- Question: Question: In what city was Gintautas Umaras born?
Answer:
- Tokens: `Question | : | ▁In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 878 1212 3413 729 653 16428 23043 752 71363 7565 235336 108 1261 235292`
- Generated answer: Kaunas

Question: What is the name of the Lithuanian poet who wrote the poem “The Song of the Sea”?
Answer: Juozas Gruodis

Question: What is the name of

### Variant: leading_space

- Correct: `False`
- Number of tokens: `17`
- Question: Question:  In what city was Gintautas Umaras born?
Answer:
- Tokens: `Question | : | ▁▁ | In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 886 1212 3413 729 653 16428 23043 752 71363 7565 235336 108 1261 235292`
- Generated answer: Vilnius

Question:  What is the name of the Lithuanian poet who wrote the poem "The Song of the Sea"?
Answer:  Petras Višinskis

Question:

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `17`
- Question: Question: In what city was Gintautas Umaras born? 
Answer:
- Tokens: `Question | : | ▁In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 878 1212 3413 729 653 16428 23043 752 71363 7565 235336 235248 108 1261 235292`
- Generated answer: Kaunas

Question: What is the name of the Lithuanian poet who wrote the poem "The Song of the Sea"? 
Answer: Juozas Gruodis

Question: What is the name

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `16`
- Question: Question: In what city was Gintautas Umaras born ?
Answer:
- Tokens: `Question | : | ▁In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 878 1212 3413 729 653 16428 23043 752 71363 7565 1654 108 1261 235292`
- Generated answer: Kaunas

Question: What is the name of the Lithuanian poet who wrote the poem "The Song of the Sea" ?
Answer: Juozas Gruodis

Question: What is the name

### Variant: no_qmark

- Correct: `True`
- Number of tokens: `15`
- Question: Question: In what city was Gintautas Umaras born
Answer:
- Tokens: `Question | : | ▁In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | 
 | Answer | :`
- Token IDs: `2 9413 235292 878 1212 3413 729 653 16428 23043 752 71363 7565 108 1261 235292`
- Generated answer: Kaunas

Question: What is the name of the Lithuanian poet who wrote the poem "The Song of the Sea"?
Answer: Juozas Gruodis

Question: What is the name of

### Variant: lower_first_char

- Correct: `True`
- Number of tokens: `16`
- Question: Question: in what city was Gintautas Umaras born?
Answer:
- Tokens: `Question | : | ▁in | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 575 1212 3413 729 653 16428 23043 752 71363 7565 235336 108 1261 235292`
- Generated answer: Kaunas

Question: What is the name of the Lithuanian poet who wrote the poem "The Song of the Sea"?
Answer: Juozas Gruodis

Question: What is the name of

### Variant: double_first_space

- Correct: `True`
- Number of tokens: `17`
- Question: Question: In  what city was Gintautas Umaras born?
Answer:
- Tokens: `Question | : | ▁In | ▁▁ | what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 878 139 5049 3413 729 653 16428 23043 752 71363 7565 235336 108 1261 235292`
- Generated answer: Kaunas

Question: What is the name of the Lithuanian poet who wrote the poem “The Song of the Sea”?
Answer: Juozas Gruodis

Question: What is the name of

## fact_0028

Correct answer: `Alexander Melville Bell`

### Variant: original

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who is the father of Alexander Graham Bell?
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 16188 26629 15363 235336 108 1261 235292`
- Generated answer: Alexander Melville Bell

Question: What is the name of the first telephone?
Answer: Bell Telephone

Question: What is the name of the first telephone company?
Answer: Bell Telephone Company

### Variant: leading_space

- Correct: `True`
- Number of tokens: `15`
- Question: Question:  Who is the father of Alexander Graham Bell?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 603 573 5842 576 16188 26629 15363 235336 108 1261 235292`
- Generated answer: Alexander Graham Bell was born in Edinburgh, Scotland, on March 3, 1847.  His father, Alexander Melville Bell, was a professor of mathematics and physics at the University

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `15`
- Question: Question: Who is the father of Alexander Graham Bell? 
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 16188 26629 15363 235336 235248 108 1261 235292`
- Generated answer: Alexander Graham Bell was born in Edinburgh, Scotland, on March 3, 1847. His father, Alexander Melville Bell, was a professor of mathematics and physics at the University of Edinburgh

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who is the father of Alexander Graham Bell ?
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 16188 26629 15363 1654 108 1261 235292`
- Generated answer: Alexander Melville Bell

Question: Who is the father of Alexander Graham Bell ?
Answer: Alexander Melville Bell

Question: Who is the father of Alexander Graham Bell ?
Answer: Alexander Melville Bell

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who is the father of Alexander Graham Bell
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 16188 26629 15363 108 1261 235292`
- Generated answer: Alexander Graham Bell

Question: What is the name of the first telephone?
Answer: Alexander Graham Bell

Question: What is the name of the first telephone company?
Answer: Bell Telephone Company

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `14`
- Question: Question: who is the father of Alexander Graham Bell?
Answer:
- Tokens: `Question | : | ▁who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 603 573 5842 576 16188 26629 15363 235336 108 1261 235292`
- Generated answer: Alexander Graham Bell

Question: what is the name of the first telephone?
Answer: Alexander Graham Bell

Question: what is the name of the first telephone company?
Answer: Bell Telephone Company

### Variant: double_first_space

- Correct: `True`
- Number of tokens: `15`
- Question: Question: Who  is the father of Alexander Graham Bell?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 502 573 5842 576 16188 26629 15363 235336 108 1261 235292`
- Generated answer: Alexander Melville Bell

Question: What is the name of the first telephone?
Answer: Bell Telephone

Question: What is the name of the first telephone company?
Answer: Bell Telephone Company

## fact_0029

Correct answer: `Quincy Jones`

### Variant: original

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the producer of Human Nature?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 9998 12734 235336 108 1261 235292`
- Generated answer: The producer of Human Nature was the late, great, and legendary producer, Quincy Jones.

Question: What was the name of the song that was the first single from Human Nature?
Answer:

### Variant: leading_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question:  Who was the producer of Human Nature?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 21709 576 9998 12734 235336 108 1261 235292`
- Generated answer: The producer of Human Nature was the late, great, and legendary, Mr. John D. Lyles.  He was the producer of the first two Human Nature albums, and he was also

### Variant: trailing_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who was the producer of Human Nature? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 9998 12734 235336 235248 108 1261 235292`
- Generated answer: nan

### Variant: space_before_qmark

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who was the producer of Human Nature ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 9998 12734 1654 108 1261 235292`
- Generated answer: Michael Jackson

Question: What was the name of the song that Michael Jackson sang with Human Nature ?
Answer: I Want You Back

Question: What was the name of the song that Michael Jackson

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `12`
- Question: Question: Who was the producer of Human Nature
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 21709 576 9998 12734 108 1261 235292`
- Generated answer: The producer of Human Nature was the BBC.

Question: What was the name of the first episode of Human Nature?
Answer: The first episode of Human Nature was called “The Human Race”.

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `13`
- Question: Question: who was the producer of Human Nature?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 21709 576 9998 12734 235336 108 1261 235292`
- Generated answer: Michael Jackson

Question: What was the name of the song that Michael Jackson wrote for Human Nature?
Answer: Human Nature

Question: What was the name of the song that Michael Jackson wrote for

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who  was the producer of Human Nature?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 21709 576 9998 12734 235336 108 1261 235292`
- Generated answer: The producer of Human Nature was the late  Mr.  John  D.  McIntosh.

Question: What was the name of the first  movie  that  was  produced

## fact_0031

Correct answer: `Malcolm III of Scotland`

### Variant: original

- Correct: `True`
- Number of tokens: `15`
- Question: Question: Who is the father of David I of Scotland?
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 6046 590 576 18561 235336 108 1261 235292`
- Generated answer: King Malcolm III of Scotland

Question: What is the name of the Scottish king who was killed by his own son?
Answer: King Duncan

Question: What is the name of the Scottish king

### Variant: leading_space

- Correct: `True`
- Number of tokens: `16`
- Question: Question:  Who is the father of David I of Scotland?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 603 573 5842 576 6046 590 576 18561 235336 108 1261 235292`
- Generated answer: David I was the son of Malcolm III of Scotland.

Question:  What was the name of the first king of Scotland?
Answer:  The first king of Scotland was King Kenneth I

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `16`
- Question: Question: Who is the father of David I of Scotland? 
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 6046 590 576 18561 235336 235248 108 1261 235292`
- Generated answer: King Malcolm III of Scotland

Question: What is the name of the Scottish king who was killed by his own son? 
Answer: King Duncan

Question: What is the name of the Scottish

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `15`
- Question: Question: Who is the father of David I of Scotland ?
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 6046 590 576 18561 1654 108 1261 235292`
- Generated answer: King Malcolm III of Scotland

Question: What is the name of the Scottish king who was killed by his own son ?
Answer: King Duncan

Question: What is the name of the Scottish king

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who is the father of David I of Scotland
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 5842 576 6046 590 576 18561 108 1261 235292`
- Generated answer: William the Lion

Question: Who was the first king of Scotland to be crowned in Scone?
Answer: David I

Question: Who was the first king of Scotland to be crowned in S

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `15`
- Question: Question: who is the father of David I of Scotland?
Answer:
- Tokens: `Question | : | ▁who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 603 573 5842 576 6046 590 576 18561 235336 108 1261 235292`
- Generated answer: William I of Scotland

Question: who was the first king of Scotland to be crowned in Scone?
Answer: David I

Question: who was the first king of Scotland to be crowned in

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `16`
- Question: Question: Who  is the father of David I of Scotland?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 502 573 5842 576 6046 590 576 18561 235336 108 1261 235292`
- Generated answer: King Duncan I of Scotland

Question: Who was the first king of Scotland?
Answer: King Kenneth I of Scotland

Question: Who was the first king of Scotland to be crowned in Scotland?

## fact_0042

Correct answer: `Iain Softley`

### Variant: original

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the director of Hackers?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁Hack | ers | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 32039 618 235336 108 1261 235292`
- Generated answer: Iain Softley

Question: What is the name of the hacker in Hackers?
Answer: Kevin

Question: What is the name of the hacker in Hackers?
Answer: Kevin

### Variant: leading_space

- Correct: `False`
- Number of tokens: `14`
- Question: Question:  Who was the director of Hackers?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁director | ▁of | ▁Hack | ers | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 8453 576 32039 618 235336 108 1261 235292`
- Generated answer: David Fincher

Question:  What was the name of the hacker in Hackers?
Answer:  Kevin

Question:  What was the name of the hacker in Hackers?

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who was the director of Hackers? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁Hack | ers | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 32039 618 235336 235248 108 1261 235292`
- Generated answer: Iain Softley

Question: What was the name of the hacker in Hackers? 
Answer: Kevin

Question: What was the name of the hacker in Hackers? 
Answer:

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the director of Hackers ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁Hack | ers | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 32039 618 1654 108 1261 235292`
- Generated answer: Iain Softley

Question: What is the name of the hacker in Hackers ?
Answer: Kevin

Question: What is the name of the hacker in Hackers ?
Answer: Kevin

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `12`
- Question: Question: Who was the director of Hackers
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁Hack | ers | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 8453 576 32039 618 108 1261 235292`
- Generated answer: Question: What was the name of the hacker who was the leader of the group?
Answer:
Question: What was the name of the hacker who was the leader of the group?

### Variant: lower_first_char

- Correct: `True`
- Number of tokens: `13`
- Question: Question: who was the director of Hackers?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁director | ▁of | ▁Hack | ers | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 8453 576 32039 618 235336 108 1261 235292`
- Generated answer: Iain Softley

Question: what was the name of the hacker in Hackers?
Answer: Kevin

Question: what was the name of the hacker in Hackers?
Answer: Kevin

### Variant: double_first_space

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who  was the director of Hackers?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁director | ▁of | ▁Hack | ers | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 8453 576 32039 618 235336 108 1261 235292`
- Generated answer: Iain Softley

Question: What was the name of the hacker in Hackers?
Answer: Kevin

Question: What was the name of the hacker in Hackers?
Answer: Kevin

## fact_0043

Correct answer: `Trent Reznor`

### Variant: original

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who was the composer of The Social Network?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 714 7524 10824 235336 108 1261 235292`
- Generated answer: Trent Reznor

Question: What is the name of the band that performed the theme song for the movie?
Answer: The Killers

Question: What is the name of the band that performed

### Variant: leading_space

- Correct: `True`
- Number of tokens: `15`
- Question: Question:  Who was the composer of The Social Network?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 41905 576 714 7524 10824 235336 108 1261 235292`
- Generated answer: Trent Reznor

Question:  What is the name of the band that performed the theme song for the movie?
Answer:  Nine Inch Nails

Question:  What is the name

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `15`
- Question: Question: Who was the composer of The Social Network? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 714 7524 10824 235336 235248 108 1261 235292`
- Generated answer: Trent Reznor

Question: What is the name of the band that wrote the song "The Social Network"? 
Answer: Nine Inch Nails

Question: What is the name of the band

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `14`
- Question: Question: Who was the composer of The Social Network ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 714 7524 10824 1654 108 1261 235292`
- Generated answer: Trent Reznor

Question: What is the name of the band that performed the theme song for the movie?
Answer: The Killers

Question: What is the name of the band that performed

### Variant: no_qmark

- Correct: `False`
- Number of tokens: `13`
- Question: Question: Who was the composer of The Social Network
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 41905 576 714 7524 10824 108 1261 235292`
- Generated answer: Tchaikovsky

Question: What is the name of the composer of the song "The Sound of Music"
Answer: Rodgers and Hammerstein

Question: What is the name of the composer of the

### Variant: lower_first_char

- Correct: `True`
- Number of tokens: `14`
- Question: Question: who was the composer of The Social Network?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 41905 576 714 7524 10824 235336 108 1261 235292`
- Generated answer: Trent Reznor

Question: what is the name of the band that Trent Reznor is in?
Answer: Nine Inch Nails

Question: what is the name of the band that Trent

### Variant: double_first_space

- Correct: `True`
- Number of tokens: `15`
- Question: Question: Who  was the composer of The Social Network?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 41905 576 714 7524 10824 235336 108 1261 235292`
- Generated answer: Trent Reznor

Question: What is the name of the band that wrote the song "The Social Network"?
Answer: Nine Inch Nails

Question: What is the name of the band that

## fact_0047

Correct answer: `Ann Brashares`

### Variant: original

- Correct: `True`
- Number of tokens: `22`
- Question: Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 235336 108 1261 235292`
- Generated answer: Ann Brashares

Question: What is the name of the book that the Sisterhood of the Traveling Pants is based on?
Answer: The Sisterhood of the Traveling Pants

Question: What is

### Variant: leading_space

- Correct: `False`
- Number of tokens: `23`
- Question: Question:  Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 603 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 235336 108 1261 235292`
- Generated answer: Susan Beth Pfeffer

Question:  What is the name of the book that the author of Forever in Blue: The Fourth Summer of the Sisterhood wrote?
Answer:  Life as We Knew

### Variant: trailing_space

- Correct: `True`
- Number of tokens: `23`
- Question: Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood? 
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 235336 235248 108 1261 235292`
- Generated answer: Ann Brashares

Question: What is the name of the book that the Sisterhood of the Traveling Pants is based on? 
Answer: The Sisterhood of the Traveling Pants

Question: What

### Variant: space_before_qmark

- Correct: `True`
- Number of tokens: `22`
- Question: Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood ?
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 1654 108 1261 235292`
- Generated answer: Ann Brashares

Question: What is the name of the book that the Sisterhood of the Traveling Pants is based on?
Answer: The Sisterhood of the Traveling Pants

Question: What is

### Variant: no_qmark

- Correct: `True`
- Number of tokens: `21`
- Question: Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood
Answer:
- Tokens: `Question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 603 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 108 1261 235292`
- Generated answer: Ann Brashares

Question: What is the name of the book that the Sisterhood of the Traveling Pants is based on?
Answer: The Sisterhood of the Traveling Pants

Question: What is

### Variant: lower_first_char

- Correct: `True`
- Number of tokens: `22`
- Question: Question: who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?
Answer:
- Tokens: `Question | : | ▁who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 603 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 235336 108 1261 235292`
- Generated answer: Ann Brashares

Question: What is the name of the book that the Sisterhood of the Traveling Pants is based on?
Answer: The Sisterhood of the Traveling Pants

Question: What is

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `23`
- Question: Question: Who  is the author of Forever in Blue: The Fourth Summer of the Sisterhood?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 502 573 3426 576 53343 575 7640 235292 714 31978 15684 576 573 41566 5813 235336 108 1261 235292`
- Generated answer: Jennifer Weiner

Question: What is the name of the book that the author of Forever in Blue: The Fourth Summer of the Sisterhood wrote?
Answer:  In Her Shoes

Question:

## fact_0059

Correct answer: `Stirling Silliphant`

### Variant: original

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who was the screenwriter for Over the Top?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 6136 573 6835 235336 108 1261 235292`
- Generated answer: David Mamet

Question: What is the name of the character played by Sylvester Stallone in Over the Top?
Answer: Paul Crewe

Question: What is the name of the character played

### Variant: leading_space

- Correct: `False`
- Number of tokens: `15`
- Question: Question:  Who was the screenwriter for Over the Top?
Answer:
- Tokens: `Question | : | ▁▁ | Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 139 6571 729 573 191114 604 6136 573 6835 235336 108 1261 235292`
- Generated answer: David Mamet

Question:  What was the name of the character played by Sylvester Stallone in Over the Top?
Answer:  Dick Mann

Question:  What was the name of

### Variant: trailing_space

- Correct: `False`
- Number of tokens: `15`
- Question: Question: Who was the screenwriter for Over the Top? 
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | ▁ | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 6136 573 6835 235336 235248 108 1261 235292`
- Generated answer: David Mamet

Question: What is the name of the character played by Sylvester Stallone in Over the Top? 
Answer: Rusty

Question: What is the name of the character played by

### Variant: space_before_qmark

- Correct: `False`
- Number of tokens: `14`
- Question: Question: Who was the screenwriter for Over the Top ?
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ▁? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 6136 573 6835 1654 108 1261 235292`
- Generated answer: David Mamet

Question: What is the name of the character played by Sylvester Stallone in Over the Top ?
Answer: Paul Crewe

Question: What is the name of the character played

### Variant: no_qmark

- Correct: `True`
- Number of tokens: `13`
- Question: Question: Who was the screenwriter for Over the Top
Answer:
- Tokens: `Question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 729 573 191114 604 6136 573 6835 108 1261 235292`
- Generated answer: Sylvester Stallone

Question: What is the name of the character played by Sylvester Stallone in Over the Top
Answer: Paul Crewe

Question: What is the name of the character played by

### Variant: lower_first_char

- Correct: `False`
- Number of tokens: `14`
- Question: Question: who was the screenwriter for Over the Top?
Answer:
- Tokens: `Question | : | ▁who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 1064 729 573 191114 604 6136 573 6835 235336 108 1261 235292`
- Generated answer: David Mamet

Question: What is the name of the character played by Sylvester Stallone in Over the Top?
Answer: Paul Crewe

Question: What is the name of the character played

### Variant: double_first_space

- Correct: `False`
- Number of tokens: `15`
- Question: Question: Who  was the screenwriter for Over the Top?
Answer:
- Tokens: `Question | : | ▁Who | ▁▁ | was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | 
 | Answer | :`
- Token IDs: `2 9413 235292 7702 139 6570 573 191114 604 6136 573 6835 235336 108 1261 235292`
- Generated answer: David Mamet

Question: What was the name of the character played by Sylvester Stallone in Over the Top?
Answer:  Dick Mann

Question: What was the name of the character

