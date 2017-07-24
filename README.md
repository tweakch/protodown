# protodown
Use markdown to generate application prototypes.

## The Idea
`protodown` is a rapid prototype generator that helps you jump start your application.

It lets you describe your main use case in a markdown file and generates your application for you.

`protodown` works, because of the `solutions` the community provides. If protodown can't find a solution for your "specific" use case, it will guide you towards a solution that works.

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
```
$ protodown resolve
> Looking for UC0... ok
> Reading use case... ok.
> Looking for solutions... found 1 solution in "core" for "python"
```

Looks for solutions of your use case for your specified language.

### Generate
```
$ protodown generate -f
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
