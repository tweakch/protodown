# protodown
Use markdown to generate application prototypes.

## The Idea
`protodown` is a prototype generator that helps you jump start your application.

`protodown` lets you describe your application in a markdown file and generates your application for you. To tell `protodown` what to generate, it expects you to define Use Case Zero (UC0).

The simplest protodown file looks like this:

```markdown
# protodown
## UC0
Hello World!
---
```
## Use Case 0
**protodown** expects you to define use case zero and guides you from there.

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
     start:    protodown.md
}
```

### Configure
```shell
$ protodown config language "csharp"
> C#
```
`protodown config` lets you configure your protodown repository.
```markdown
# protodown.config
{
  start:    protodown.md
  language: csharp
}

---
```

### Generate
Open `protodown.md` and write your "Use Case 0" in Markdown: 

```markdown
# protodown
## UC0
Hello world!
```

To generate the C# scaffolding from the markdown in protodown.md use:
```shell
$ protodown -fg protodown.md
> Generating UC0... done!
```

## About
Prototyping is an important part in software development. A prototype lets you test ideas and see what road you want to go down.

You can save a lot of time, when you write good prototypes, because the scaffolding of a successful prototype will often be used as starting point for the first iterations of your application.
