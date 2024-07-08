# Objective
- Build an LLM agent  (AI agent!) that generates data which will be used later for finetuning LLMs

# From docker
```
$ docker pull poptropicasahil/llm-agents-datacreation:latest
```

## Internals
- Anthropic's Claude model is the LLM agent used internally
- User will have to provide their API credentials from OPENROUTER (https://openrouter.ai/)
- We use Docker to containerise the application and also upload it to the Docker hub
- No finetuning, just using the LLMs API


## Technicals

# To run the code, you should run
```
$ docker run -it -v {input-directory-path}:/app/data llm-agents
```
* `-it`: it is iterative and requires user inputs multiple times
* `-v`: because we have to provide input data (like a docker volume path)
* `llm-agents`: name of the docker image

for example, for me it is `docker run -it -v C:\Users\Admin\Documents\TMP\CODE\LLM-Agents-Claude\datasets:/app/data llm-agents`



## TODO
* Check if logging can be enabled and given to the user instead of console prints
* Nicer Readme
* Upload to the hub
* Use docker volumes
