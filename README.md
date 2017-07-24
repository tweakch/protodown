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
> Initialized empty repository.
```

### Configure
```
$ protodown config language "python"
```

### Resolve
```
$ protodown resolve
> Looking for UC0... ok
> Reading use case... ok.
> Looking for solutions... found 1 solution in "core" for "python"
```

### Generate
```
$ protodown generate
> Generating prototype... done!
```

### Run
```
$ protodown run
> Running python application "Hello World"...

> Hello World!
```

That's it!

For more information on each step of the workflow, checkout the wiki pages.

## About
Prototyping is an important part in software development. A prototype lets you test ideas and see what road you want to go down.

You can save a lot of time when you write good prototypes, because the scaffolding of a successful prototype will often be used as starting point for the first iterations of your application.

`protodown` tries to help you write quality prototypes with as little effort as possible.
