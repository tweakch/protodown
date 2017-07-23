# protodown
Use markdown to generate application prototypes.

## The Idea
`protodown` is a prototype generator that helps you jump start your application.

It lets you describe your main use case in a markdown file and generates your application for you.

## The Workflow
Use the `protodown` command to initialize, configure and generate your prototype.

### Initialize
```shell
$ protodown init
> Done.
```
By default `protodown init` creates two files in your current directory:
- the `protodown.md` file
```markdown
# protodown
## UC0
Hello world!
```
- and the `protodown.config` file
```markdown
# protodown.config
{
    "start": "protodown.md"
}
```

### Configure
To configure your prototype, use the `config` command.

```shell
$ protodown config language "csharp"
> C#
```

This command adds a language section to your `protodown.config` file.
```markdown
# protodown.config
{
    "start": "protodown.md",
    "solutions": [
        "https://github.com/tweakch/protodown/blob/master/SOLUTIONS.md",
    ],
    "language": [
        "csharp"
    ]
}
```

### Resolve
Open `protodown.md` and change the default "Use Case 0" to your needs.  

```markdown
# protodown
## UC0
Download a file
```

`protodown` will verify that the supplied file contains a UC0 and looks for a solution of your use case online.
```shell
$ protodown resolve protodown.md
> Looking for UC0... ok
> Looking for solutions... found 1 solution for csharp
```

Of course you can tell `protodown` where to look for solutions.
```shell
$ protodown config solutions /path/to/your/solutions.md
```

This will add a new entry to the solutions section of your `protodown.config` file:
```markdown
# protodown.config
{
    "start": "protodown.md",
    "language": [
        "csharp"
    ],
    "solutions": [
        "https://github.com/tweakch/protodown/blob/master/solutions.md",
        "/path/to/your/solutions.md"
    ]
}
```

### Generate
Since we have
```shell
$ protodown generate
> Generating prototype... done!
```

## About
Prototyping is an important part in software development. A prototype lets you test ideas and see what road you want to go down.

You can save a lot of time, when you write good prototypes, because the scaffolding of a successful prototype will often be used as starting point for the first iterations of your application.
