# xkcd936

Convert cumbersome strings into memorable phrases.

## Installation

```
pip install xkcd936
```

## Usage

```
from xkcd936 import visualize
memorable_str = visualize('k2dhE4hd@!Y')
```

## About

This generator performs an MD5 hash of the input. The resulting bits are used
to choose a grammatical template:

-   article adj adj animal
-   adj article adj animal

The dictionary can be upgraded to include patterns like:

-   verb article adj noun
-   article adj adj noun
-   article adv adj noun
-   adv verb article noun

and a word for each slot.

The total space is around 43 bits. This may not sound like much, but it
doesn't matter.

Software doesn't just run on the computer -- it also runs in each of your
users' heads. For many problems with user-facing software, "adding more bits"
is the wrong solution. The right solution often involves tapping into the
user's natural cognitive and social capabilities.

## License

Released under MIT license.
