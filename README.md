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
OK, this worked first time with ChatGPT 4 - but it cost 11cents for Day1. Does feel a waste of inference servers for day1 of advent of code... but let's see where this goes 😄

But tbf, I am loading in quite a bit of the puzzle input which it probably doesn't need to understand the formatting! I'll refine this for day2

It would also be awesome to try qwen-coder locally as I predict it could perform similarly to the server giants.