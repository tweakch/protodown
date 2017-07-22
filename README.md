# protodown
Use markdown to generate application scaffolds and prototypes.

## The Idea
Prototyping is an important part in software development. A prototype lets you test ideas and see what road you want to go down.

You can save a lot of time, when you write good prototypes, because the scaffolding of a successful prototype will often be used as starting point for the first iterations of your application.

**protodown** lets you describe your prototype in markdown - following a set of simple rules - and generates the scaffolding of your application for you.

## The Basics
A prototype tries to demonstrate that something you want to do can work or not.

Good prototypes cut right through the core functionality of your application and demonstrate by **proof of concept** that what you want to do with your code can work.

But writing a good prototype is hard work. Especially the first one. When faced with a complex problem finding a good point to start is difficult.   

I believe that, when developing prototypes, one should start with the definition of Use Case Zero (UC0).

### Use Case Zero
UC0 is the simplest sentence you can think of, that describes what your prototype wants to do.

For example: 
- "Ask the user for an URL and download the HTML."
- "Get the title of the top trending video on YouTube."
- "CRUD a car-object using the MVVM pattern."

**protodown** expects you to define your use case zero and guides you from there.

## The Workflow
Simply write up your Use Case 0 into a Markdown file and save it: 

```markdown
# protodown
## UC0: your main goal
Generate application scaffolding from a single Markdown file.
```
And then use the `protodown` command to initialize, configure and generate your prototype.

### Initialize
```shell
$ protodown init
> Done.
```
`$ protodown init` creates the default `protodown.config` file in the current directory.

### Configure
```shell
$ protodown config language "csharp"
> C#
```
`protodown config` sets the programming language for your application to C#.

### Generate
```shell
$ protodown -fg protodown.md
```
`protodown -fg protodown.md` generates the C# scaffolding from the markdown in protodown.md.
