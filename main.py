"""Famous Last Words at 1 Percent: write the funniest one-line farewell
a phone could say as its battery hits 1 percent."""

LINE = "Goodbye. I have been at 1% for twenty minutes. I was lying to you the whole time."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-199 characters,
    # not only white space.
    if not (1 <= len(LINE) <= 199):
        raise ValueError("entry must be 1-199 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
