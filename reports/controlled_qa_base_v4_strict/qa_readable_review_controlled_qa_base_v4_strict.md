# QA readable review — controlled_qa_base_v4_strict

- Switching facts: 13
- Switching rows: 91
- Correct switching rows: 48
- Wrong switching rows: 43

## fact_0001

**Correct answer:** George Frideric Handel
**Possible answers:** ["George Frideric Handel", "Handel", "G. F. Handel", "Georg Friedrich Händel", "George Frederick Handel", "G. F. Händel", "Händel", "George Frideric"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | George Frideric Handel | George Frideric Handel |
| leading_space | False | Joseph Haydn | nan |
| trailing_space | True | George Frideric Handel | George Frideric Handel |
| space_before_qmark | True | George Frideric Handel | George Frideric Handel |
| no_qmark | False | Delibes | nan |
| lower_first_char | True | George Frideric Handel | George Frideric Handel |
| double_first_space | False | Joseph Haydn | nan |

## fact_0002

**Correct answer:** Warren Beatty
**Possible answers:** ["Warren Beatty", "Henry Warren Beaty", "Henry Warren Beatty"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | False | Dalton Trumbo | nan |
| leading_space | True | Warren Beatty | Warren Beatty |
| trailing_space | False | Dalton Trumbo | nan |
| space_before_qmark | False | Dalton Trumbo | nan |
| no_qmark | False | Dalton Trumbo | nan |
| lower_first_char | False | Dalton Trumbo | nan |
| double_first_space | False | Dalton Trumbo | nan |

## fact_0004

**Correct answer:** John Kander
**Possible answers:** ["John Kander", "John Harold Kander"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | False | Kander and Ebb | nan |
| leading_space | False | Kander and Ebb | nan |
| trailing_space | False | Kander and Ebb | nan |
| space_before_qmark | False | Kander and Ebb | nan |
| no_qmark | False | Kander and Ebb | nan |
| lower_first_char | False | Kander and Ebb | nan |
| double_first_space | True | John Kander and Fred Ebb | John Kander |

## fact_0007

**Correct answer:** Nuri Bilge Ceylan
**Possible answers:** ["Nuri Bilge Ceylan"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Uzak was written by the famous Turkish screenwriter, Nuri Bilge Ceylan. | Nuri Bilge Ceylan |
| leading_space | False | Yılmaz Güney | nan |
| trailing_space | False | nan | nan |
| space_before_qmark | True | Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan. | Nuri Bilge Ceylan |
| no_qmark | True | Uzak was written by the famous Turkish screenwriter, writer and director, Nuri Bilge Ceylan. | Nuri Bilge Ceylan |
| lower_first_char | False | Question: What is the name of the character played by the actor who plays the role of the father in Uzak? Answer: | nan |
| double_first_space | False | Yılmaz Güney | nan |

## fact_0013

**Correct answer:** Oliver Stone
**Possible answers:** ["Oliver Stone", "William Oliver Stone"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Oliver Stone | Oliver Stone |
| leading_space | False | Jim Morrison | nan |
| trailing_space | True | Oliver Stone | Oliver Stone |
| space_before_qmark | True | Oliver Stone | Oliver Stone |
| no_qmark | True | Oliver Stone | Oliver Stone |
| lower_first_char | True | Oliver Stone | Oliver Stone |
| double_first_space | True | Oliver Stone | Oliver Stone |

## fact_0017

**Correct answer:** Kaunas
**Possible answers:** ["Kaunas", "Kovno", "Kovne", "Kovna", "Kowno", "Kauen"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Kaunas | Kaunas |
| leading_space | False | Vilnius | nan |
| trailing_space | True | Kaunas | Kaunas |
| space_before_qmark | True | Kaunas | Kaunas |
| no_qmark | True | Kaunas | Kaunas |
| lower_first_char | True | Kaunas | Kaunas |
| double_first_space | True | Kaunas | Kaunas |

## fact_0028

**Correct answer:** Alexander Melville Bell
**Possible answers:** ["Alexander Melville Bell"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Alexander Melville Bell | Alexander Melville Bell |
| leading_space | True | Alexander Graham Bell was born in Edinburgh, Scotland, on March 3, 1847.  His father, Alexander Melville Bell, was a professor of mathematics and physics at the University | Alexander Melville Bell |
| trailing_space | True | Alexander Graham Bell was born in Edinburgh, Scotland, on March 3, 1847. His father, Alexander Melville Bell, was a professor of mathematics and physics at the University of Edinburgh | Alexander Melville Bell |
| space_before_qmark | True | Alexander Melville Bell | Alexander Melville Bell |
| no_qmark | False | Alexander Graham Bell | nan |
| lower_first_char | False | Alexander Graham Bell | nan |
| double_first_space | True | Alexander Melville Bell | Alexander Melville Bell |

## fact_0029

**Correct answer:** Quincy Jones
**Possible answers:** ["Quincy Jones", "Q", "Quincy", "Quincy Delight Jones Jr.", "Quincy Jones Jr."]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | The producer of Human Nature was the late, great, and legendary producer, Quincy Jones. | Quincy Jones |
| leading_space | False | The producer of Human Nature was the late, great, and legendary, Mr. John D. Lyles.  He was the producer of the first two Human Nature albums, and he was also | nan |
| trailing_space | False | nan | nan |
| space_before_qmark | False | Michael Jackson | nan |
| no_qmark | False | The producer of Human Nature was the BBC. | nan |
| lower_first_char | False | Michael Jackson | nan |
| double_first_space | False | The producer of Human Nature was the late  Mr.  John  D.  McIntosh. | nan |

## fact_0031

**Correct answer:** Malcolm III of Scotland
**Possible answers:** ["Malcolm III of Scotland", "Malcolm Canmore"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | King Malcolm III of Scotland | Malcolm III of Scotland |
| leading_space | True | David I was the son of Malcolm III of Scotland. | Malcolm III of Scotland |
| trailing_space | True | King Malcolm III of Scotland | Malcolm III of Scotland |
| space_before_qmark | True | King Malcolm III of Scotland | Malcolm III of Scotland |
| no_qmark | False | William the Lion | nan |
| lower_first_char | False | William I of Scotland | nan |
| double_first_space | False | King Duncan I of Scotland | nan |

## fact_0042

**Correct answer:** Iain Softley
**Possible answers:** ["Iain Softley", "Iain Declan Softley"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Iain Softley | Iain Softley |
| leading_space | False | David Fincher | nan |
| trailing_space | True | Iain Softley | Iain Softley |
| space_before_qmark | True | Iain Softley | Iain Softley |
| no_qmark | False | Question: What was the name of the hacker who was the leader of the group? Answer: | nan |
| lower_first_char | True | Iain Softley | Iain Softley |
| double_first_space | True | Iain Softley | Iain Softley |

## fact_0043

**Correct answer:** Trent Reznor
**Possible answers:** ["Trent Reznor", "Michael Trent Reznor"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Trent Reznor | Trent Reznor |
| leading_space | True | Trent Reznor | Trent Reznor |
| trailing_space | True | Trent Reznor | Trent Reznor |
| space_before_qmark | True | Trent Reznor | Trent Reznor |
| no_qmark | False | Tchaikovsky | nan |
| lower_first_char | True | Trent Reznor | Trent Reznor |
| double_first_space | True | Trent Reznor | Trent Reznor |

## fact_0047

**Correct answer:** Ann Brashares
**Possible answers:** ["Ann Brashares"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | True | Ann Brashares | Ann Brashares |
| leading_space | False | Susan Beth Pfeffer | nan |
| trailing_space | True | Ann Brashares | Ann Brashares |
| space_before_qmark | True | Ann Brashares | Ann Brashares |
| no_qmark | True | Ann Brashares | Ann Brashares |
| lower_first_char | True | Ann Brashares | Ann Brashares |
| double_first_space | False | Jennifer Weiner | nan |

## fact_0059

**Correct answer:** Stirling Silliphant
**Possible answers:** ["Stirling Silliphant", "Stirling Dale Silliphant", "Sylvester Stallone", "Sly Stallone", "Sylvester Enzio Stallone", "Michael Sylvester Gardenzio Stallone"]

| variant_id | is_correct | strict_answer_segment | matched_answer |
|---|---:|---|---|
| original | False | David Mamet | nan |
| leading_space | False | David Mamet | nan |
| trailing_space | False | David Mamet | nan |
| space_before_qmark | False | David Mamet | nan |
| no_qmark | True | Sylvester Stallone | Sylvester Stallone |
| lower_first_char | False | David Mamet | nan |
| double_first_space | False | David Mamet | nan |
