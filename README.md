> protodown is a side project. It will not move very quickly... but I try to *push* myself. 

# protodown
Use markdown to generate application prototypes.

## The Idea
`protodown` is a rapid prototype generator that helps you jump start your application.

It lets you describe your use cases in a markdown file and generates your application for you. The generated code always tries to follow best practices of software development.

`protodown` works, because of the `solutions` the community provides. If protodown can't find a solution for your "specific" use case, it will guide you towards a similar solution that already worked.

## The Workflow
Use the `protodown` command to `initialize`, `configure`, `resolve`, `generate` and `run` your prototype.

### Initialize
```
$ protodown init
> Initialized repository.
```

Creates a default protodown.md file. This file describes the use case of your prototype.
```markdown
# protodown
## UC0
Hello world!
```

### Configure
```
$ protodown config language "python"
```

Adds a `language` element to your `protodown.config` file;

```json
# protodown.config
{
  "language": "csharp"
}
```

### Resolve
With `resolve` you can look for solutions of your use case.

```
$ protodown resolve
> Looking for UC0... ok
> Reading use case... ok.
> Looking for "python" solutions... found 2 solution(s) in "core"
```

> Development Notice: This is really where the magic happens... I don't really know how protodown will scale when people work on more complex solutions. But I will gladly take your suggestions and feedback on how to improve protodown.

### Generate
```
$ protodown generate --use-first-solution
> Generating prototype... done!
```
Generate the folders and files for your prototype.

### Run
```
$ protodown run
> Running python application "Hello World"...

> Hello World!
```

That's it!

For more information on each step of the workflow, checkout the wiki pages.

<p align="center">
	<a href="https://travis-ci.org/tweakch/protodown/"><img src="https://travis-ci.org/tweakch/protodown.svg?branch=master" /> </a>
</p>
