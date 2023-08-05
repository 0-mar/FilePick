
"""
Spusť tento skript pro kontrolu úkolu
"""

import os.path
import sys
import sifrovani_priklad

correct = """This was a triumph!
I'm making a note here:
Huge success!

It's hard to overstate
my satisfaction.

Aperture Science:
We do what we must
because we can
For the good of all of us.
Except the ones who are dead.

But there's no sense crying
over every mistake.
You just keep on trying
'til you run out of cake.
And the science gets done.
And you make a neat gun
for the people who are
still alive.

I'm not even angry...
I'm being so sincere right now.
Even though you broke my heart,
and killed me.

And tore me to pieces.
And threw every piece into a fire.
As they burned it hurt because
I was so happy for you!

Now, these points of data
make a beautiful line.
And we're out of beta.
We're releasing on time!
So I'm GLaD I got burned!
Think of all the things we learned!
for the people who are
still alive.

Go ahead and leave me...
I think I'd prefer to stay inside...
Maybe you'll find someone else
to help you.
Maybe Black Mesa?
That was a joke. Ha Ha. Fat Chance!

Anyway this cake is great!
It's so delicious and moist!

Look at me: still talking
when there's science to do!
When I look out there,
it makes me glad I'm not you.

I've experiments to run.
There is research to be done.
On the people who are
still alive.
And believe me I am
still alive.
I'm doing science and I'm
still alive.
I feel fantastic and I'm
still alive.
While you're dying I'll be
still alive.
And when you're dead I will be
still alive

Still alive.

Still alive.
"""


def test():
    sys.argv = []
    sys.argv.append("sifrovani_priklad.py")
    sys.argv.append("sifrovani_priklad.py")
    sys.argv.append("sifrovani_priklad.py")
    sys.argv.append("sifrovani_priklad.py")

    sys.argv[1] = os.path.join("xorcrypt", "aperture.key")
    sys.argv[2] = os.path.join("xorcrypt", "aperture.xor")
    sys.argv[3] = "tmp.txt"

    sifrovani_priklad.xorcrypt(sys.argv[1], sys.argv[2], sys.argv[3])

    with open("tmp.txt") as file:
        assert file.read() == correct, "Neshoduje se obsah souboru"


if __name__ == '__main__':
    test()
