# Tarot Poem

- link to html file download: https://drive.google.com/drive/folders/1xxymcOID4b6gssvpgJbsaoQeieacmupW?usp=sharing
- Above there is a video file which shows how the webpage looks like named Webpage Video.
- link to Colab: https://colab.research.google.com/drive/1w4nr_zpSuWXzjzlW3GNfN_cNG1O4Avnv?usp=sharing
- Credit:
- https://labyrinthos.co/blogs/tarot-card-meanings-list
- https://www.shortpoems.org/poems/fate/
- https://www.tarot.com/tarot/cards/major-arcana

![b7a47ac4e92b45e823cfdee0f5972fa](https://user-images.githubusercontent.com/58541110/152698942-65359db0-6d20-4a89-89d7-f916a6d877ee.png)

![0f3c426763c5ebc2f37f626e12b918c](https://user-images.githubusercontent.com/58541110/152698945-33c7b35a-c81c-402f-8b31-9a9670482688.png)

## Why I Choose this Topic

- The project <Tarot Poem> is an algorithm-generated poem that is based on the theme of Tarot fortune telling. Tarot is a type of ancient divination that uses playcards to predict the future. The basic rule is that each Tarot card has its own unique illustration and name, which represents a certain type of meaning. For example, the card "The magician" means trickery and illusions. The Taroists use their own interpretation on several cards they draw and then associate it with real life to make predictions.  The first reason for choosing Tarot as the topic is that Tarot and poetry share similarities in some way. They are both ancient wisdom, subjective, and abstract to many people. Both tarot reading and poem reading provokes a lot of imagination as they both often use a large amount of metaphor techniques. The second reason is that I regard the process of tarot reading a form of collage. By drawing several cards with separate meanings, the taroist combine the fragments of meanings into a whole picture, and then develops his/her own predictions. Therefore, I believe the theme will fit with "Assemblage" very well.

## Why This Format
- The webpage format I choose is HTML and I also choose github for documentation and writing. The reason for HTML is that I want to give the users a feeling of drawing the tarot cards on their own. So the in the first opening page, you can click a button to see the poem. I put one output in the webpage, and for future improvement, I will make it do instant random generating stead of just showing the outputs. Choosing github documentation is because as a project of computer-generated poem, the github fits with the technology perspective well. I can also put my original files in the repository, which makes the documentation clear and convenient for future reference.   
  
## How the Algorithm Works
  
- My poems have 3 blocks, and each block contains 4 lines in a total of 12 lines. The three blocks are the tarot reading based on three randomly-picked tarot cards, which represents your past, your present and your future. In the first line, I get a list of card names through scraping. Then I write the print('%s represents your Past'/Present Future%tarot_past) to randomly put the card name. In the second line, the respective key words are generated — it writes like “The card goes reversed, a sign of lack of center and lost inner voice” (the upright direction and reversed direction of tarot cards are different in meanings). I use re.sub and re.split to clean up the lists. 
- For the third line, I use Textblob to write grammar. The words are from the website detailed tarot explanations. The format is “ noun+verbs+adjective+noun”. Finally for the last line, I randomly picked lines which contained the word “fate” or “fortune” using Regular Expressions. 
- In Conclusion, the first and second lines are interpretations of tarot cards. For the third line I recompose the detailed explanations into one format. And the last line extend the topic to the discussion of fate. 

## How the Output Different to Human Piece
- The output is much more abstract than human works, which leaves space for thoughts. Also, it jumps out some cliches of poem writing. For example, I really like one sentence I generated —— ‘Answers seek the inner answers’. Many poem writers avoid using repetitive words in one poem. However, I think the repetition here is very nice, which indicates that you should stop seeking answers even if you have already got one. 
  
## Thoughts/Feelings Provoked
- I believe that my output will provoke a deep thinking on the conditions of your current life. By reading this abstract poem about fate and fortune, you can have a piece of time to reconsider what you have done so far, what you are doing, and what you are going to do. Divination is not only about superstitions, rather, it is a healing tool that can help you give away all the distractions and focus on your inner heart to make your life decisions. Since the language of the tarot poem is abstract, you can actually have multiple interpretations. Although it might offer you some good directions, your life is still totally on your own.
  
## My Thoughts on Production Process
 - This project is really a challenge for me as a Python beginner. There are lots of unprecdicted obstacles due to my lack of knowledge. Also, the scraping is complicated as we cannot always get a very clean list. Therefore, we have to process a lot by using re.sub of re.split, which is time-consuming. The result is surprisng, and I really improve a lot on Python. 

