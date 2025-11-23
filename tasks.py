from invoke import task


@task
def start(ctx):
    ctx.run("python -m src.index")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")


@task(coverage)
def robot(ctx):
    ctx.run("robot src/robot_tests")


@task(coverage)
def robot_headless(ctx):
    ctx.run("robot --variable HEADLESS:true src/robot_tests")
