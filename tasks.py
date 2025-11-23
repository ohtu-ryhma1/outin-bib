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
def robot_tests(ctx):
    ctx.run("robot src/robot_tests")
