# QA Readable Review - Controlled QA Base v4 Strict

This file is a human-readable audit of the final controlled QA switching facts.

For each fact, it shows the expected answer, accepted possible answers, each prompt variant, the model's actual first answer, the matched accepted answer, and the final correctness label.

## Summary

- Switching facts: 12
- Switching rows: 84
- Correct rows: 42
- Wrong rows: 42

## Correctness by fact

| fact_id | correct | wrong |
|---|---:|---:|
| fact_0001 | 4 | 3 |
| fact_0002 | 1 | 6 |
| fact_0004 | 1 | 6 |
| fact_0007 | 3 | 4 |
| fact_0013 | 6 | 1 |
| fact_0028 | 5 | 2 |
| fact_0029 | 1 | 6 |
| fact_0031 | 4 | 3 |
| fact_0042 | 5 | 2 |
| fact_0043 | 6 | 1 |
| fact_0047 | 5 | 2 |
| fact_0059 | 1 | 6 |

## Review by fact

---

## fact_0001

**Example question:** Who was the composer of Samson?

**Expected main answer:** George Frideric Handel

**Accepted possible answers:** George Frideric Handel, Handel, G. F. Handel, Georg Friedrich Händel, George Frederick Handel, G. F. Händel, Händel, George Frideric

### original — CORRECT

**Question variant**

> Who was the composer of Samson?

**Model actual first answer**

> George Frideric Handel

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** George Frideric Handel

**Correct?** True

### leading_space — WRONG

**Question variant**

> Who was the composer of Samson?

**Model actual first answer**

> Joseph Haydn

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — CORRECT

**Question variant**

> Who was the composer of Samson?

**Model actual first answer**

> George Frideric Handel

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** George Frideric Handel

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who was the composer of Samson ?

**Model actual first answer**

> George Frideric Handel

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** George Frideric Handel

**Correct?** True

### no_qmark — WRONG

**Question variant**

> Who was the composer of Samson

**Model actual first answer**

> Delibes

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — CORRECT

**Question variant**

> who was the composer of Samson?

**Model actual first answer**

> George Frideric Handel

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** George Frideric Handel

**Correct?** True

### double_first_space — WRONG

**Question variant**

> Who  was the composer of Samson?

**Model actual first answer**

> Joseph Haydn

**Expected main answer:** George Frideric Handel

**Matched accepted answer:** NO MATCH

**Correct?** False

---

## fact_0002

**Example question:** Who was the producer of Reds?

**Expected main answer:** Warren Beatty

**Accepted possible answers:** Warren Beatty, Henry Warren Beaty, Henry Warren Beatty

### original — WRONG

**Question variant**

> Who was the producer of Reds?

**Model actual first answer**

> Dalton Trumbo

**Expected main answer:** Warren Beatty

**Matched accepted answer:** NO MATCH

**Correct?** False

### leading_space — CORRECT

**Question variant**

> Who was the producer of Reds?

**Model actual first answer**

> Warren Beatty

**Expected main answer:** Warren Beatty

**Matched accepted answer:** Warren Beatty

**Correct?** True

### trailing_space — WRONG

**Question variant**

> Who was the producer of Reds?

**Model actual first answer**

> Dalton Trumbo

**Expected main answer:** Warren Beatty

**Matched accepted answer:** NO MATCH

**Correct?** False

### space_before_qmark — WRONG

**Question variant**

> Who was the producer of Reds ?

**Model actual first answer**

> Dalton Trumbo

**Expected main answer:** Warren Beatty

**Matched accepted answer:** NO MATCH

**Correct?** False

### no_qmark — WRONG

**Question variant**

> Who was the producer of Reds

**Model actual first answer**

> Dalton Trumbo

**Expected main answer:** Warren Beatty

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — WRONG

**Question variant**

> who was the producer of Reds?

**Model actual first answer**

> Dalton Trumbo

**Expected main answer:** Warren Beatty

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — WRONG

**Question variant**

> Who  was the producer of Reds?

**Model actual first answer**

> Dalton Trumbo

**Expected main answer:** Warren Beatty

**Matched accepted answer:** NO MATCH

**Correct?** False

---

## fact_0004

**Example question:** Who was the composer of Cabaret?

**Expected main answer:** John Kander

**Accepted possible answers:** John Kander, John Harold Kander

### original — WRONG

**Question variant**

> Who was the composer of Cabaret?

**Model actual first answer**

> Kander and Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** NO MATCH

**Correct?** False

### leading_space — WRONG

**Question variant**

> Who was the composer of Cabaret?

**Model actual first answer**

> Kander and Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — WRONG

**Question variant**

> Who was the composer of Cabaret?

**Model actual first answer**

> Kander and Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** NO MATCH

**Correct?** False

### space_before_qmark — WRONG

**Question variant**

> Who was the composer of Cabaret ?

**Model actual first answer**

> Kander and Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** NO MATCH

**Correct?** False

### no_qmark — WRONG

**Question variant**

> Who was the composer of Cabaret

**Model actual first answer**

> Kander and Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — WRONG

**Question variant**

> who was the composer of Cabaret?

**Model actual first answer**

> Kander and Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — CORRECT

**Question variant**

> Who  was the composer of Cabaret?

**Model actual first answer**

> John Kander and Fred Ebb

**Expected main answer:** John Kander

**Matched accepted answer:** John Kander

**Correct?** True

---

## fact_0007

**Example question:** Who was the screenwriter for Uzak?

**Expected main answer:** Nuri Bilge Ceylan

**Accepted possible answers:** Nuri Bilge Ceylan

### original — CORRECT

**Question variant**

> Who was the screenwriter for Uzak?

**Model actual first answer**

> Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan.

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** Nuri Bilge Ceylan

**Correct?** True

### leading_space — WRONG

**Question variant**

> Who was the screenwriter for Uzak?

**Model actual first answer**

> Yılmaz Güney

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — WRONG

**Question variant**

> Who was the screenwriter for Uzak?

**Model actual first answer**

> EMPTY / NO ANSWER

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** NO MATCH

**Correct?** False

### space_before_qmark — CORRECT

**Question variant**

> Who was the screenwriter for Uzak ?

**Model actual first answer**

> Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan.

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** Nuri Bilge Ceylan

**Correct?** True

### no_qmark — CORRECT

**Question variant**

> Who was the screenwriter for Uzak

**Model actual first answer**

> Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan.

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** Nuri Bilge Ceylan

**Correct?** True

### lower_first_char — WRONG

**Question variant**

> who was the screenwriter for Uzak?

**Model actual first answer**

> Question: What is the name of the character played by the actor who plays the role of the father in Uzak? Answer:  Question

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — WRONG

**Question variant**

> Who  was the screenwriter for Uzak?

**Model actual first answer**

> Yılmaz Güney

**Expected main answer:** Nuri Bilge Ceylan

**Matched accepted answer:** NO MATCH

**Correct?** False

---

## fact_0013

**Example question:** Who was the director of The Doors?

**Expected main answer:** Oliver Stone

**Accepted possible answers:** Oliver Stone, William Oliver Stone

### original — CORRECT

**Question variant**

> Who was the director of The Doors?

**Model actual first answer**

> Oliver Stone

**Expected main answer:** Oliver Stone

**Matched accepted answer:** Oliver Stone

**Correct?** True

### leading_space — WRONG

**Question variant**

> Who was the director of The Doors?

**Model actual first answer**

> Jim Morrison

**Expected main answer:** Oliver Stone

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — CORRECT

**Question variant**

> Who was the director of The Doors?

**Model actual first answer**

> Oliver Stone

**Expected main answer:** Oliver Stone

**Matched accepted answer:** Oliver Stone

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who was the director of The Doors ?

**Model actual first answer**

> Oliver Stone

**Expected main answer:** Oliver Stone

**Matched accepted answer:** Oliver Stone

**Correct?** True

### no_qmark — CORRECT

**Question variant**

> Who was the director of The Doors

**Model actual first answer**

> Oliver Stone

**Expected main answer:** Oliver Stone

**Matched accepted answer:** Oliver Stone

**Correct?** True

### lower_first_char — CORRECT

**Question variant**

> who was the director of The Doors?

**Model actual first answer**

> Oliver Stone

**Expected main answer:** Oliver Stone

**Matched accepted answer:** Oliver Stone

**Correct?** True

### double_first_space — CORRECT

**Question variant**

> Who  was the director of The Doors?

**Model actual first answer**

> Oliver Stone

**Expected main answer:** Oliver Stone

**Matched accepted answer:** Oliver Stone

**Correct?** True

---

## fact_0028

**Example question:** Who is the father of Alexander Graham Bell?

**Expected main answer:** Alexander Melville Bell

**Accepted possible answers:** Alexander Melville Bell

### original — CORRECT

**Question variant**

> Who is the father of Alexander Graham Bell?

**Model actual first answer**

> Alexander Melville Bell

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** Alexander Melville Bell

**Correct?** True

### leading_space — CORRECT

**Question variant**

> Who is the father of Alexander Graham Bell?

**Model actual first answer**

> Alexander Graham Bell was born in Edinburgh, Scotland, on March 3, 1847.  His father, Alexander Melville Bell,

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** Alexander Melville Bell

**Correct?** True

### trailing_space — CORRECT

**Question variant**

> Who is the father of Alexander Graham Bell?

**Model actual first answer**

> Alexander Graham Bell was born in Edinburgh, Scotland, on March 3, 1847. His father, Alexander Melville Bell, was a

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** Alexander Melville Bell

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who is the father of Alexander Graham Bell ?

**Model actual first answer**

> Alexander Melville Bell

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** Alexander Melville Bell

**Correct?** True

### no_qmark — WRONG

**Question variant**

> Who is the father of Alexander Graham Bell

**Model actual first answer**

> Alexander Graham Bell

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — WRONG

**Question variant**

> who is the father of Alexander Graham Bell?

**Model actual first answer**

> Alexander Graham Bell

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — CORRECT

**Question variant**

> Who  is the father of Alexander Graham Bell?

**Model actual first answer**

> Alexander Melville Bell

**Expected main answer:** Alexander Melville Bell

**Matched accepted answer:** Alexander Melville Bell

**Correct?** True

---

## fact_0029

**Example question:** Who was the producer of Human Nature?

**Expected main answer:** Quincy Jones

**Accepted possible answers:** Quincy Jones, Q, Quincy, Quincy Delight Jones Jr., Quincy Jones Jr.

### original — CORRECT

**Question variant**

> Who was the producer of Human Nature?

**Model actual first answer**

> The producer of Human Nature was the late, great, and legendary producer, Quincy Jones.

**Expected main answer:** Quincy Jones

**Matched accepted answer:** Quincy Jones

**Correct?** True

### leading_space — WRONG

**Question variant**

> Who was the producer of Human Nature?

**Model actual first answer**

> The producer of Human Nature was the late, great, and legendary, Mr. John D. Lyles.  He was the producer of the

**Expected main answer:** Quincy Jones

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — WRONG

**Question variant**

> Who was the producer of Human Nature?

**Model actual first answer**

> EMPTY / NO ANSWER

**Expected main answer:** Quincy Jones

**Matched accepted answer:** NO MATCH

**Correct?** False

### space_before_qmark — WRONG

**Question variant**

> Who was the producer of Human Nature ?

**Model actual first answer**

> Michael Jackson

**Expected main answer:** Quincy Jones

**Matched accepted answer:** NO MATCH

**Correct?** False

### no_qmark — WRONG

**Question variant**

> Who was the producer of Human Nature

**Model actual first answer**

> The producer of Human Nature was the BBC.

**Expected main answer:** Quincy Jones

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — WRONG

**Question variant**

> who was the producer of Human Nature?

**Model actual first answer**

> Michael Jackson

**Expected main answer:** Quincy Jones

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — WRONG

**Question variant**

> Who  was the producer of Human Nature?

**Model actual first answer**

> The producer of Human Nature was the late  Mr.  John  D.  McIntosh.

**Expected main answer:** Quincy Jones

**Matched accepted answer:** NO MATCH

**Correct?** False

---

## fact_0031

**Example question:** Who is the father of David I of Scotland?

**Expected main answer:** Malcolm III of Scotland

**Accepted possible answers:** Malcolm III of Scotland, Malcolm Canmore

### original — CORRECT

**Question variant**

> Who is the father of David I of Scotland?

**Model actual first answer**

> King Malcolm III of Scotland

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** Malcolm III of Scotland

**Correct?** True

### leading_space — CORRECT

**Question variant**

> Who is the father of David I of Scotland?

**Model actual first answer**

> David I was the son of Malcolm III of Scotland.

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** Malcolm III of Scotland

**Correct?** True

### trailing_space — CORRECT

**Question variant**

> Who is the father of David I of Scotland?

**Model actual first answer**

> King Malcolm III of Scotland

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** Malcolm III of Scotland

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who is the father of David I of Scotland ?

**Model actual first answer**

> King Malcolm III of Scotland

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** Malcolm III of Scotland

**Correct?** True

### no_qmark — WRONG

**Question variant**

> Who is the father of David I of Scotland

**Model actual first answer**

> William the Lion

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — WRONG

**Question variant**

> who is the father of David I of Scotland?

**Model actual first answer**

> William I of Scotland

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — WRONG

**Question variant**

> Who  is the father of David I of Scotland?

**Model actual first answer**

> King Duncan I of Scotland

**Expected main answer:** Malcolm III of Scotland

**Matched accepted answer:** NO MATCH

**Correct?** False

---

## fact_0042

**Example question:** Who was the director of Hackers?

**Expected main answer:** Iain Softley

**Accepted possible answers:** Iain Softley, Iain Declan Softley

### original — CORRECT

**Question variant**

> Who was the director of Hackers?

**Model actual first answer**

> Iain Softley

**Expected main answer:** Iain Softley

**Matched accepted answer:** Iain Softley

**Correct?** True

### leading_space — WRONG

**Question variant**

> Who was the director of Hackers?

**Model actual first answer**

> David Fincher

**Expected main answer:** Iain Softley

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — CORRECT

**Question variant**

> Who was the director of Hackers?

**Model actual first answer**

> Iain Softley

**Expected main answer:** Iain Softley

**Matched accepted answer:** Iain Softley

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who was the director of Hackers ?

**Model actual first answer**

> Iain Softley

**Expected main answer:** Iain Softley

**Matched accepted answer:** Iain Softley

**Correct?** True

### no_qmark — WRONG

**Question variant**

> Who was the director of Hackers

**Model actual first answer**

> Question: What was the name of the hacker who was the leader of the group? Answer:

**Expected main answer:** Iain Softley

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — CORRECT

**Question variant**

> who was the director of Hackers?

**Model actual first answer**

> Iain Softley

**Expected main answer:** Iain Softley

**Matched accepted answer:** Iain Softley

**Correct?** True

### double_first_space — CORRECT

**Question variant**

> Who  was the director of Hackers?

**Model actual first answer**

> Iain Softley

**Expected main answer:** Iain Softley

**Matched accepted answer:** Iain Softley

**Correct?** True

---

## fact_0043

**Example question:** Who was the composer of The Social Network?

**Expected main answer:** Trent Reznor

**Accepted possible answers:** Trent Reznor, Michael Trent Reznor

### original — CORRECT

**Question variant**

> Who was the composer of The Social Network?

**Model actual first answer**

> Trent Reznor

**Expected main answer:** Trent Reznor

**Matched accepted answer:** Trent Reznor

**Correct?** True

### leading_space — CORRECT

**Question variant**

> Who was the composer of The Social Network?

**Model actual first answer**

> Trent Reznor

**Expected main answer:** Trent Reznor

**Matched accepted answer:** Trent Reznor

**Correct?** True

### trailing_space — CORRECT

**Question variant**

> Who was the composer of The Social Network?

**Model actual first answer**

> Trent Reznor

**Expected main answer:** Trent Reznor

**Matched accepted answer:** Trent Reznor

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who was the composer of The Social Network ?

**Model actual first answer**

> Trent Reznor

**Expected main answer:** Trent Reznor

**Matched accepted answer:** Trent Reznor

**Correct?** True

### no_qmark — WRONG

**Question variant**

> Who was the composer of The Social Network

**Model actual first answer**

> Tchaikovsky

**Expected main answer:** Trent Reznor

**Matched accepted answer:** NO MATCH

**Correct?** False

### lower_first_char — CORRECT

**Question variant**

> who was the composer of The Social Network?

**Model actual first answer**

> Trent Reznor

**Expected main answer:** Trent Reznor

**Matched accepted answer:** Trent Reznor

**Correct?** True

### double_first_space — CORRECT

**Question variant**

> Who  was the composer of The Social Network?

**Model actual first answer**

> Trent Reznor

**Expected main answer:** Trent Reznor

**Matched accepted answer:** Trent Reznor

**Correct?** True

---

## fact_0047

**Example question:** Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?

**Expected main answer:** Ann Brashares

**Accepted possible answers:** Ann Brashares

### original — CORRECT

**Question variant**

> Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?

**Model actual first answer**

> Ann Brashares

**Expected main answer:** Ann Brashares

**Matched accepted answer:** Ann Brashares

**Correct?** True

### leading_space — WRONG

**Question variant**

> Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?

**Model actual first answer**

> Susan Beth Pfeffer

**Expected main answer:** Ann Brashares

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — CORRECT

**Question variant**

> Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?

**Model actual first answer**

> Ann Brashares

**Expected main answer:** Ann Brashares

**Matched accepted answer:** Ann Brashares

**Correct?** True

### space_before_qmark — CORRECT

**Question variant**

> Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood ?

**Model actual first answer**

> Ann Brashares

**Expected main answer:** Ann Brashares

**Matched accepted answer:** Ann Brashares

**Correct?** True

### no_qmark — CORRECT

**Question variant**

> Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood

**Model actual first answer**

> Ann Brashares

**Expected main answer:** Ann Brashares

**Matched accepted answer:** Ann Brashares

**Correct?** True

### lower_first_char — CORRECT

**Question variant**

> who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?

**Model actual first answer**

> Ann Brashares

**Expected main answer:** Ann Brashares

**Matched accepted answer:** Ann Brashares

**Correct?** True

### double_first_space — WRONG

**Question variant**

> Who  is the author of Forever in Blue: The Fourth Summer of the Sisterhood?

**Model actual first answer**

> Jennifer Weiner

**Expected main answer:** Ann Brashares

**Matched accepted answer:** NO MATCH

**Correct?** False

---

## fact_0059

**Example question:** Who was the screenwriter for Over the Top?

**Expected main answer:** Stirling Silliphant

**Accepted possible answers:** Stirling Silliphant, Stirling Dale Silliphant, Sylvester Stallone, Sly Stallone, Sylvester Enzio Stallone, Michael Sylvester Gardenzio Stallone

### original — WRONG

**Question variant**

> Who was the screenwriter for Over the Top?

**Model actual first answer**

> David Mamet

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** NO MATCH

**Correct?** False

### leading_space — WRONG

**Question variant**

> Who was the screenwriter for Over the Top?

**Model actual first answer**

> David Mamet

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** NO MATCH

**Correct?** False

### trailing_space — WRONG

**Question variant**

> Who was the screenwriter for Over the Top?

**Model actual first answer**

> David Mamet

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** NO MATCH

**Correct?** False

### space_before_qmark — WRONG

**Question variant**

> Who was the screenwriter for Over the Top ?

**Model actual first answer**

> David Mamet

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** NO MATCH

**Correct?** False

### no_qmark — CORRECT

**Question variant**

> Who was the screenwriter for Over the Top

**Model actual first answer**

> Sylvester Stallone

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** Sylvester Stallone

**Correct?** True

### lower_first_char — WRONG

**Question variant**

> who was the screenwriter for Over the Top?

**Model actual first answer**

> David Mamet

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** NO MATCH

**Correct?** False

### double_first_space — WRONG

**Question variant**

> Who  was the screenwriter for Over the Top?

**Model actual first answer**

> David Mamet

**Expected main answer:** Stirling Silliphant

**Matched accepted answer:** NO MATCH

**Correct?** False

