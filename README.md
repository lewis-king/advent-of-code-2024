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
As a quick workaround I just send the full context of the description (including Part 1) to the LLM for Part 2, but the better solution would be to store the previous message i.e Part 1 in chat history.

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
