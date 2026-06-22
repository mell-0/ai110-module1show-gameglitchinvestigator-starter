# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed. * = working, @ = done

|     Input    | Expected Behavior | Actual Behavior | Console Output / Error |
|--------------|-------------------|-----------------|------------------------|
|>@ Pressed new|> Reset my tries & |> Does nothing   |
|game          | make a new round  |                 |
|              |                   |                 |
|>@ Submited    |> hint is supposed |> Gives me wrong |
|a guess       |to be correct      |hints            |
|              |                   |                 | 
|>@ Pressed     |> No guesses when  |> Allows you to  | 
|submit guess  |attempt reaches 0  | guess past 0    |
|when there's  |                   |                 |  
|no input\bad  |                   |                 |
|input         |                   |                 |  
|              |                   |                 | 
|> Pressed new |> history is       |> Keeps past     |
|game          |supposed to reset  |inputs in history|
|              |                   |                 |
|> Attemps not |> Show out of      |> Showing out of |
|matching up   |attempt message    |attempt message  |
|              |when you're out of |when you still   |
|              |attempts           |have 1 left      |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Answer: I used Claude code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Answer: When sending the secret, the program was converting it into a string. Claude said the program doesn't need to covert the secret to string for every other guess. I 
verified the suggestion by testing various inputs to see if the program behaved correctly.  

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Answer: When I asked ai to fix a bug where the number of guesses is delayed by one input. Ai suggested st.form. I tried and it didn't work.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Answer: I tried out all the edge cases that I could think of.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Answer: I ran the test_parse_guess_valid_integer test & it showed me if the parse_guess accepted the a basic integer

- Did AI help you design or understand any tests? How?

Answer: It helped me come up with edge cases that I haven't considered yet.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Answer: Streamlit is a script that re-runs top to bottom every time something happens and st.session_state is a dictionary that persists across reruns for a single user's browser session. I would think of it as a backpack the user carries, it survives each script restart.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Answer: One habit that I would reuse in future labs is asking ai for one small defined task at a time, similar to git commits. 
  This makes it easier for me to understand the changes.

- What is one thing you would do differently next time you work with AI on a coding task?

Answer: I could use the different modes better. Planning mode would be helpful if I'm preparing to make bigger changes

- In one or two sentences, describe how this project changed the way you think about AI generated code.

Answer: I think ai generated code has come along way. It writes code that I would write or even better sometimes. 
