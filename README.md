# advent-of-code-2024

Going a bit rogue this year but want to continue spending more time working with LLMs!
So...
Plan is to create an auto-solver which self-solves each day for me 😈

## Anthropic Computer Use
### Running 🏃‍♂️

```shell
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

OK so this was interesting, I'll share the results shortly. But it couldn't quite self-solve, it came up with a solution but the wrong answer and then I kept getting rate limited.

SO..... next option is simple LLM-assisted based approach to see how that fares!

LLM of choosing.. make me an AoC solver!...
## LLM Assisted 🔮
### Day1 
OK, this worked first time with ChatGPT 4 - but it cost 11cents for Day1 (see day2 for why so much!). Does feel a waste of inference servers for day1 of advent of code... but let's see where this goes 😄

But tbf, I am loading in quite a bit of the puzzle input which it probably doesn't need to understand the formatting! I'll refine this for day2

It would also be awesome to try qwen-coder locally as I predict it could perform similarly to the server giants.

### Day2
On Day1 I was being speculative and only providing Part 2 to the LLM to solve Part 2.
This didn't work for Day 2 as it needed the context from Part 1 too.
As a quick workaround I just send the full context of the description (including Part 1) to the LLM for Part 2, but the better solution would be to store the previous message i.e Part 1 in memory.

Billing - 16cents! - OK I had to dig more, so I'm using gpt-4 which is now an older model and you get charged at a higher rate: input/ouput: gpt-4 $30.00 / 1M tokens $60.00 / 1M tokens.

OK so I'm paying more for using a worse model, but now I know that, I've updated to 4o the best model from OpenAPI at the time of writing which is: gpt-4o
$2.50 / 1M input tokens
$1.25 / 1M input tokens
$1.25 / 1M cached** input tokens

So with future days I'm going to play a bit with the models to see how they perform on smaller/cheaper models i.e 4o-mini which is priced at:
gpt-4o-mini
$0.150 / 1M input tokens
$0.075 / 1M input tokens
$0.075 / 1M cached** input tokens

### Day3
Had to escape the curley braces which was messing with the prompt creation, but apart from that, within roughly 3 secs gpt-4o produced another working solution first time

Part 2 - OK the LLM took a couple of iterations this time (I later realised I accidently reverted back to using the more expensive/not as good gpt-4 so this could explain why it required more work!), I updated the solver to store the history of what we tried and made it interactive, so I could tell it the wrong answer it was giving. Based on a wrong answer the LLM would then try a new solution given the feedback. It looks something like this:
```
Human: No it gave 328 which was incorrect
System: Here is an improved Python solution
System: The previous solution attempted to match the 'do()' and 'don't()' instructions from the current position in the string, which would not find instructions that began before the current position. The improved solution uses the re.search() method to find the most recent 'do()' or 'don't()' instruction in the string up to the current position. Also, after matching a 'mul()' instruction, it skips the characters that are part of the matched instruction to avoid matching the same instruction multiple times.
Human: hmm this still got the same wrong answer 328
System: I apologize for the confusion earlier. Here is the revised Python solution that handles both the "mul" operation and the "do" and "don't" instructions correctly.
System: This program reads the corrupted memory and processes the instructions in the order they appear. It keeps track of whether the 'mul' instructions are enabled or not based on the most recent 'do' or 'don't' instruction. When it encounters a 'mul' instruction and if 'mul' is enabled, it multiplies the two numbers and adds the result to a running total. It repeats this process until it has processed all the instructions in the corrupted memory.
```

After 2 failed attempts it was able to produce the correct solution. - I've also started storing all solution attempts to see how the LLM evolved its solution

accidentally used 2 models (4o for part1 and 4 for part 2):
gpt4 - 22cents
gpt4o - 1cents!
As you can see the gulf in pricing diff. So we'll make sure 4o is being used or smaller similar ability models from now on.


### Day4
Part 1 - solved first time with gpt-4o

Part 2 - This was causing all sorts of problems for the LLM! gpt4o kept coming up with the same couple of answers after 7 attempts!
So I switched to Claude-3.5-sonnet to see how it would fare, and it came up with different answers but was still failing after a few attempts.
This one may require some actual human understanding to further guide the LLM! Stay tuned...

Total cost incurred so far:
gpt-4o = $0.09
claude-3.5-sonnet = $0.25

So even though I'm making way more attempts, at least I'm using cheaper models now.

The LLM struggled a huge deal with part 2.
I need to improve the debug verbosity so that I can get a clearer understanding off the full context going to the LLM.
But I wasn't having much luck with prompt engineering here.
I ended up implementing the solution myself (see human_takeover file). The LLM wasn't getting to any kind of nice solution here and struggled completely.

I would have expected some prompt engineering to coerce it to a solution here, so that's why I made the note about improving debug verbosity as I'm not sure if the solver is not doing exactly as I expect.
One to look into!

### Day5
Part 1 - solved first time with gpt-4o

Part 2 - solved first time with gpt-4o

Time taken = 15 secs overall

Cost - 7 cents - I think now is the time to try how cheaper models fair for these coding tasks. 4o probably is overkill.

**NB: I've realised I'm doing things a bit inefficiently with creating two separate solution files for Part 1 and 2. Going forward I'll pass the working solution of part 1 to part 2's LLM prompt so that the solution is modified to cater for both, rather than building from scratch.**

### Day6
Part 1 - solved first time with gpt-4o

Part 2 - solved first time with gpt-4o - however, I've updated the prompt to make the LLM produce answers for both part 1 and part 2 after modifying the solution for part 1. And it actually got part 1 wrong and part 2 right with this new solution.
So I'll need to tweak this bit!!

Cost - 7 cents - still need to use a slimmer model! But I'm just loving the quick decent results atm with 4o

### Day7
Part 1 - solved first time with gpt-4o

Part 2 - solved first time with gpt-4o

### Day8
Part 1 - gpt-4o is struggling with this one.
I tweaked the prompt to allow extra spacing between the sample inputs so that the description text or prompt text did not mess with the solution.
And after a retry this worked first time!

Part 2 - Solved first time

Moral of this one - take extra care when formatting the information required for the LLM to do its job. We pass in a sequence of text, and if that sequence contains different sources/information types you should try to ensure they are separated. This was particularly important for the LLM to understand the sample inputs scope.