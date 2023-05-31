# Big Data Foundations project

I am a student in the third and final year of university and I work on a project
for a "Big Data Foundations" course. The project consists of analyzing a dataset
and writing a report for it.

## Tools

I use Python for analyzing the dataset. I use numpy for linear algebra and
pandas for data processing. You may suggest other libraries that I can use.

## Dataset

The dataset is called "TMDB 15000 Movies Dataset" and it's header columns are:

- movie_id - Integer
- original_title - String
- overview - String
- popularity - Float
- release_date - String (I convert this to datetime via `pd.to_datetime(df['release_date'], errors='coerce')`)
- title - String
- vote_average - Float
- vote_count - Integer
- genres - JSON array of objects of format {id: Integer, name: String}
- keywords - JSON array of strings

### Examples for the `genre` column

```json
[{'id': 28, 'name': 'Action'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}]
```

```json
[{'id': 28, 'name': 'Action'}, {'id': 80, 'name': 'Crime'}, {'id': 53, 'name': 'Thriller'}]
```

```json
[{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 53, 'name': 'Thriller'}]
```

### Examples for the `keywords` column

```json
['remake', 'looop lapeta', 'saade saati']
```

```json
['police', 'sequel', 'police officer', 'cop universe']
```

```json
['spy', 'fake death', 'spy thriller', 'spy universe', 'yrf spy universe']
```

### Dataset sample

```csv
movie_id,original_title,overview,popularity,release_date,title,vote_average,vote_count,genres,keywords
1005112,Happy Sorry Day,Akash is an egoistic man who can’t say sorry to anyone and for the same reason he's facing marital issues. His life changes when he meets an 8-year-old girl named Sohana during a journey.,1.4,2022-01-14,Happy Sorry Day,10.0,1,[],[]
943443,Ribbons for Peace,"""Made in the aftermath of Indian and Pakistani nuclear tests, Ribbons gives new meaning to an old film song by Kishore Kumar – a kind of “Imagine” composed before the days of John Lennon.  With guest appearances by well-known movie stars like Naseeruddin Shah, Aamir Khan, Kittu Gidwani and Chandrachur, the film was made to counter a pro-nuke music video made by the political party in power.""",0.6,1998-01-01,Ribbons for Peace,0.0,0,[],[]
238,The Godfather,"Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",106.435,1972-03-14,The Godfather,8.7,17733,"[{'id': 18, 'name': 'Drama'}, {'id': 80, 'name': 'Crime'}]","['italy', 'loss of loved one', 'love at first sight', 'based on novel or book', 'europe', 'symbolism', 'patriarch', 'organized crime', 'mafia', 'lawyer', 'religion', 'revenge motive', 'crime family', 'sicilian mafia', 'religious hypocrisy', 'gun violence', 'rise to power', 'dead horse', 'gang violence', '1940s', '1950s', 'mafia war', 'part of trilogy']"
278,The Shawshank Redemption,"Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",99.374,1994-09-23,The Shawshank Redemption,8.7,23583,"[{'id': 18, 'name': 'Drama'}, {'id': 80, 'name': 'Crime'}]","['prison', 'corruption', 'police brutality', 'based on novel or book', 'prison cell', 'delinquent', 'parole board', 'prison escape', 'wrongful imprisonment', 'framed for murder', '1940s', 'voiceover']"
240,The Godfather Part II,"In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",62.216,1974-12-20,The Godfather Part II,8.6,10740,"[{'id': 18, 'name': 'Drama'}, {'id': 80, 'name': 'Crime'}]","['italy', 'italian american', 'cuba', 'symbolism', 'gangster', 'melancholy', 'praise', 'revenge', 'organized crime', 'mafia', 'lawyer', 'suburb', 'corrupt politician']"
424,Schindler's List,The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.,56.746,1993-12-15,Schindler's List,8.6,13947,"[{'id': 18, 'name': 'Drama'}, {'id': 36, 'name': 'History'}, {'id': 10752, 'name': 'War'}]","['based on novel or book', 'factory', 'concentration camp', 'hero', 'holocaust (shoah)', 'ss (nazi schutzstaffel)', 'world war ii', 'ghetto', 'jew persecution', 'kraków, poland', 'auschwitz-birkenau concentration camp', 'industrialist', 'nazi', 'defense industry', 'biography', 'based on true story', 'historical fiction', 'train', 'poland', 'weapons manufacturer']"
389,12 Angry Men,"The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",37.811,1957-04-10,12 Angry Men,8.5,7173,"[{'id': 18, 'name': 'Drama'}]","['judge', 'jurors', 'sultriness', 'death penalty', 'father murder', 'puerto rico', 'anonymity', 'court case', 'heat', 'class', 'innocence', 'court', 'based on play or musical', 'black and white', 'courtroom', 'courtroom drama', 'one location']"
155,The Dark Knight,"Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",86.357,2008-07-14,The Dark Knight,8.5,29497,"[{'id': 18, 'name': 'Drama'}, {'id': 28, 'name': 'Action'}, {'id': 80, 'name': 'Crime'}, {'id': 53, 'name': 'Thriller'}]","['crime fighter', 'secret identity', 'anti hero', 'scarecrow', 'sadism', 'chaos', 'vigilante', 'joker', 'superhero', 'based on comic', 'tragic hero', 'organized crime', 'anti villain', 'criminal mastermind', 'district attorney', 'super power', 'super villain', 'neo-noir']"
497,The Green Mile,"A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",75.86,1999-12-10,The Green Mile,8.5,15264,"[{'id': 14, 'name': 'Fantasy'}, {'id': 18, 'name': 'Drama'}, {'id': 80, 'name': 'Crime'}]","['southern usa', 'mentally disabled', 'based on novel or book', 'death row', 'jail guard', 'great depression', 'supernatural', 'psychopath', 'prison guard', 'jail', 'electric chair', 'torture', 'magic realism', 'healing', '1930s', 'abuse of power']"
```

## Requirements

You will perform several tasks so as to help me elaborate the project.

1. Identify one or more research questions of interest for a business audience
   based on the dataset that I chose.
2. Determine what other steps may be needed to prepare dataset for applying
   scientific methods of data analysis on it so as to obtain alternative models
   which can be useful for answering questions proposed in step 1.
3. Propose at least two data analysis methods that I can experiment with for the
   purpose of creating alternative models for answering the questions proposed
   in step 1.

Based on the questions you propose in step 1, other preparation steps proposed
in step 2 and the data analysis methods proposed in step 3 I will run
experiments and create alternative models. I will then choose a validation
methodology to determine the most suitable method and model. I will then draw
business conclusions by answering the questions proposed in step 1 based on the
results of my experiments and my model and method of choice. You are free to
help me with any of these tasks as well.

Say "Ready!" when you feel confident you can start helping me.
