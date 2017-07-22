# protodown
An experimental project using markdown to generate application prototypes
***

## The Idea
Prototyping is one of the most important steps in development. It lets you test ideas and see what road you want to go down.

Most of the time, successful prototypes will be used as a scaffold for the first iteration of your application.

**protodown** lets you describe your prototype in words - following a set of simple rules - and then generate the scaffolding for your application.

## The Basics
Every application development process starts with the definition of a first use case - UC0: your main goal. **protodown** expects you to define your main use case first and guides you from there.

## The Workflow
Simply write up your main usecase into a Markdown file.: 

```
# protodown
## UC0: your main goal
Generate application scaffolding from a single Markdown file.
```
Save your markdown to a file (here: protodown.md) and use the `protodown` command to initialize your protodown repository.

```
protodown init
protodown -fg protodown.md
```

`$ protodown init` creates the .pdn folder in the current directory and initializes the `protodown.config` file with some basic configurations.

Set the progamming language for your application with `protodown config`.
```
$ protodown config language "csharp"
> C#
```

`protodown -fg protodown.md` generates the C# scaffolding from of the markdown in protodown.md.
