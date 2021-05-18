import click
import pandas as pd


@click.command()
@click.argument(
    "input"
)
@click.option(
    "-o", "--output", required=False, default="output.csv", help="output csv",
)
@click.option(
    "-a",
    "--add",
    required=False,
    default=None,
    help="columns to add in the format COLNAME1=VAL,COLNAME2=VAL",
)
@click.option(
    "-d",
    "--drop",
    required=False,
    default=None,
)
@click.option(
    "-k",
    "--keep",
    required=False,
    default=None,
)
def main(input, output, add, drop, keep):
    spl = input.split(",")
    dfs = []
    for fname in spl:
        dfs.append(pd.read_csv(fname))
    df = pd.concat(dfs)
    if drop is not None:
        spl = drop.split(",")
        for col in spl:
            df = df.drop(col, axis=1)
    if keep is not None:
        cols = df.columns
        spl = keep.split(",")
        for c in cols:
            if c not in spl:
                df = df.drop(c, axis=1)
    if add is not None:
        spl = add.split(",")
        for colinfo in spl:
            name,val = colinfo.split("=")
            df[name] = val

    df.to_csv(output, index=False)


if __name__ == "__main__":
    main()
