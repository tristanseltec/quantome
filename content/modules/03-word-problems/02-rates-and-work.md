+++
summary = "Solve GMAT rate problems with D = RT tables, average and relative speed, and additive work rates, including pipes and drains, workers who start or stop at different times, and machine-production questions."
+++

# Rates & Work

Rate problems are the most common word-problem family on the GMAT, and they all rest on one equation. Whether a car is covering miles, a pipe is filling a tank, or a machine is stamping bolts, the amount done equals the rate multiplied by the time. What makes the problems hard is not the equation but the bookkeeping: several movers, several legs of a trip, workers who join late or leave early, and averages that are not the averages you expect.

This chapter turns that bookkeeping into a routine. It assumes the translation habits from [Translating words into equations](../translating-words-into-equations/), and it uses fractions freely; if adding $\tfrac16 + \tfrac19$ is slow for you, review [Fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/) first.

## Key ideas

> [!IMPORTANT]
> $$\text{Distance} = \text{Rate} \times \text{Time} \qquad \text{Work} = \text{Rate} \times \text{Time}$$
> The second equation is the first one with "distance" replaced by "amount of job done".

### The units of rate

A rate is always "something **per** unit of time": miles per hour, litres per minute, widgets per hour, or "jobs per hour". Writing the units next to every number is the best protection against errors, because units multiply and cancel like algebra:

$$
45\ \frac{\text{pages}}{\text{min}} \times 60\ \frac{\text{min}}{\text{h}} = 2{,}700\ \frac{\text{pages}}{\text{h}}.
$$

For work problems, the unit of work is **one job**. If Ana paints a room in 5 hours, her rate is $\tfrac15$ room per hour. **Time and rate are reciprocals** when the job is one unit: a 5-hour worker has rate $\tfrac15$, and a worker with rate $\tfrac{2}{15}$ needs $\tfrac{15}{2} = 7.5$ hours.

> [!WARNING]
> Never add or average **times**. Two people who each take 6 hours do not take 12 hours together, or 6. You add **rates**: $\tfrac16 + \tfrac16 = \tfrac13$, so they take 3 hours.

### The D = RT table

For any problem with more than one mover or more than one leg, draw a table with one row per mover (or leg) and columns R, T, D. Fill in what you know, use a variable for one unknown, and express everything else in terms of it. Each row obeys $R \times T = D$, and the problem's sentences give you the relationships **between** rows (same distance, total time, a head start).

| | Rate | Time | Distance |
|---|---|---|---|
| Cyclist | 12 | $t + 1.5$ | $12(t + 1.5)$ |
| Car | 48 | $t$ | $48t$ |

The table above sets up Example 2 below: the car leaves 1.5 hours later, and "catches up" means the distances are equal.

### Average speed, and why it is a harmonic mean

Average speed is defined as

$$
\text{average speed} = \frac{\text{total distance}}{\text{total time}}.
$$

It is **not** the average of the speeds in general. Suppose you travel the same distance $d$ at speed $a$ and then at speed $b$. The total time is $\tfrac{d}{a} + \tfrac{d}{b}$, so

$$
\bar v = \frac{2d}{\frac{d}{a} + \frac{d}{b}} = \frac{2}{\frac1a + \frac1b} = \frac{2ab}{a + b}.
$$

The $d$ cancels, so the distance doesn't matter. This expression is the **harmonic mean** of $a$ and $b$. For 40 mph out and 60 mph back, $\bar v = \tfrac{2 \cdot 40 \cdot 60}{100} = 48$, not 50.

Why is it lower than the ordinary average? You spend **more time** at the slower speed (the slow leg of equal length takes longer), so the slow speed gets more weight. Average speed is a time-weighted average of the speeds:

$$
\bar v = \frac{a t_1 + b t_2}{t_1 + t_2}.
$$

This gives two rules:

- **Equal times** → average speed is the ordinary mean $\tfrac{a + b}{2}$.
- **Equal distances** → average speed is the harmonic mean $\tfrac{2ab}{a + b}$, always below the ordinary mean when $a \ne b$.

> [!TIP]
> On equal-distance problems, **pick a convenient distance**: the least common multiple of the speeds. For 40 and 60 mph, use 120 miles each way: 3 hours out, 2 back, 240 miles in 5 hours, 48 mph. No formula to remember.

### Relative speed

When two objects move along the same line, think about the **gap** between them and how fast it changes.

- **Toward each other** (or apart in opposite directions): the gap changes at $r_1 + r_2$.
- **Same direction** (one catching the other): the gap changes at $r_1 - r_2$ (faster minus slower).

Then $\text{time} = \dfrac{\text{gap}}{\text{rate of change of the gap}}$. Two trains 330 miles apart heading toward each other at 50 and 60 mph meet after $330 / 110 = 3$ hours.

For catching up, the gap is the **head start**: the distance the leader covered before the chaser set off. A cyclist with a 1.5-hour head start at 12 mph is 18 miles ahead; a car at 48 mph closes that at $48 - 12 = 36$ mph, taking half an hour.

On a **circular track**, runners going in opposite directions meet each time their combined distance grows by one lap; runners in the same direction meet each time the faster gains one full lap.

Boats in a current and planes in a wind are relative speed too: downstream speed is $b + c$ and upstream speed is $b - c$, where $b$ is the speed in still water and $c$ the current. So $b$ is the average of the downstream and upstream speeds, and $c$ is half their difference.

### Round trips

A round trip has two legs of **equal distance**, so the harmonic-mean rule applies. Problems often give the total time and ask for the distance: with speeds $a$ and $b$ and total time $T$,

$$
\frac{d}{a} + \frac{d}{b} = T.
$$

Or they give the average speed you want and ask how fast the return leg must be. That second version has a surprise: if you go out at 30 mph, no return speed can make the round-trip average 60 mph, because you would need to finish the return leg in zero time.

### Work rates add

If A completes a job in $a$ hours and B in $b$ hours, then working together their rates add:

$$
\frac1a + \frac1b = \frac1t \quad\Rightarrow\quad t = \frac{ab}{a + b}.
$$

This works because in one hour A does $\tfrac1a$ of the job and B does $\tfrac1b$; the job does not care who does which part. The formula $\tfrac{ab}{a+b}$ (product over sum) is handy for two workers. For three or more, add the reciprocals.

Two sanity checks always hold. The combined time is **less than the faster worker's time** alone. And it is **more than half** the faster worker's time (two copies of the faster worker would take exactly half).

### Pipes and drains

A drain is a worker with a **negative** rate. If pipe A fills a tank in 3 hours, pipe B in 6 hours, and a drain empties a full tank in 4 hours, the net rate with all three open is

$$
\frac13 + \frac16 - \frac14 = \frac{4 + 2 - 3}{12} = \frac14 \text{ tank per hour}.
$$

If the net rate is negative, the tank empties; if it is zero, the level never changes.

### Working together, then one leaves (and different start times)

When workers start or stop at different times, split the job into **phases**. In each phase, compute (combined rate) × (phase length) = fraction of the job done. The fractions of all phases add up to 1.

Equivalently, track each worker separately: **each worker's contribution is their rate times the time they actually worked**, and the contributions sum to 1 job:

$$
\frac{t_A}{a} + \frac{t_B}{b} = 1.
$$

This second form is often quicker. For instance, if A (12 hours alone) works from 8:00 to 1:00, A does $\tfrac{5}{12}$ of the job, so B (8 hours alone) must do $\tfrac{7}{12}$, which takes $\tfrac{7}{12} \times 8 = 4\tfrac23$ hours: B started at 8:20.

### Rate-of-production problems

"If 6 machines produce 720 bolts in 4 hours..." problems are proportional reasoning. Find the rate of **one** machine for **one** hour (the "unit rate"), then scale:

$$
\text{output} = (\text{number of machines}) \times (\text{rate per machine}) \times (\text{time}).
$$

Here one machine makes $\tfrac{720}{6 \times 4} = 30$ bolts per hour. Then 9 machines make 1,620 bolts in $\tfrac{1620}{9 \times 30} = 6$ hours. Output is proportional to machines and to time; time needed is **inversely** proportional to the number of machines.

> [!TIP]
> When a problem uses only letters ("$m$ machines make $b$ bolts in $h$ hours; how long for $k$ machines to make $c$ bolts?"), **pick numbers**. Choose values that divide nicely, compute the answer, then test each answer choice with the same numbers. Exactly one should match. If two match, pick new numbers and test only those two.

### Common traps

> [!WARNING]
> The wrong answer choices on rate problems are usually built from:
> 1. **Averaging speeds** instead of dividing total distance by total time.
> 2. **Adding or averaging times** instead of adding rates.
> 3. **Mixed units**: minutes and hours, or miles per hour and feet per second.
> 4. **Ignoring the head start**: forgetting that the leader was already moving before the chaser began.
> 5. **Adding instead of subtracting** relative speeds (or the reverse), for same-direction versus opposite-direction motion.
> 6. **Answering the wrong time**: the number of hours when the question asked for the clock time, or the time *after* B joined when it asked *when* B joined.

> [!NOTE]
> Readers using Claude Code can check a finished solution with the `quantome-math` plugin (`/plugin install quantome-math@quantome`). Set up the table yourself first; the exam gives you no help.

## Worked examples

### Example 1 *(Easy)*

A driver travels 120 miles from Town A to Town B at an average speed of 40 miles per hour and returns along the same route at an average speed of 60 miles per hour. What is the average speed for the round trip, in miles per hour?

(A) 45 (B) 48 (C) 50 (D) 52 (E) 100

**Solution.** Total distance 240 miles. Time out $120 / 40 = 3$ hours, time back $120 / 60 = 2$ hours. Average speed $= 240 / 5 = 48$ mph. The answer is **(B)**.

With the formula: $\tfrac{2 \cdot 40 \cdot 60}{40 + 60} = \tfrac{4800}{100} = 48$. Choice (C) is the trap "average of 40 and 60"; choice (E) is the sum of the speeds. Note that the correct answer is below 50, as it must be: more time is spent at 40 mph.

### Example 2 *(Medium)*

A cyclist leaves a village at 9:00 a.m. and rides along a straight road at a constant 12 miles per hour. At 10:30 a.m., a car leaves the same village and follows the same road at a constant 48 miles per hour. At what time does the car catch up with the cyclist?

(A) 10:45 a.m. (B) 11:00 a.m. (C) 11:15 a.m. (D) 11:30 a.m. (E) 12:00 noon

**Solution (relative speed).** By 10:30, the cyclist has a 1.5-hour head start: $12 \times 1.5 = 18$ miles. The car closes the gap at $48 - 12 = 36$ mph, taking $18 / 36 = 0.5$ hours. The car catches up at **11:00 a.m.**, choice **(B)**.

**Solution (table).** Let the car drive for $t$ hours; the cyclist has then ridden $t + 1.5$ hours. Equal distances: $48t = 12(t + 1.5)$, so $36t = 18$ and $t = 0.5$. Same answer.

The gap to close is the cyclist's 18-mile head start, and it closes at the *difference* of the speeds because both are moving the same way. Using the sum (60 mph) would give 18 minutes, and forgetting the head start altogether gives nonsense; the relative-speed view avoids both.

### Example 3 *(Medium)*

Working alone, Asha can paint a fence in 6 hours and Bilal can paint it in 9 hours. They work together for 2 hours, and then Asha leaves. How many more hours does Bilal need to finish the fence alone?

(A) 2 (B) 3 (C) 4 (D) 5 (E) 6

**Solution.** Combined rate $\tfrac16 + \tfrac19 = \tfrac{3 + 2}{18} = \tfrac{5}{18}$ fence per hour. In 2 hours they paint $\tfrac{10}{18} = \tfrac59$. The remaining $\tfrac49$ at Bilal's rate $\tfrac19$ per hour takes **4 hours**: **(C)**.

**Faster (contributions).** Asha works 2 hours and does $\tfrac26 = \tfrac13$ of the job. Bilal does the other $\tfrac23$, which takes him $\tfrac23 \times 9 = 6$ hours in total. He has already worked 2 of them, so he needs 4 more. Choice (E), 6, is Bilal's total time, not the additional time.

### Example 4 *(Hard)*

An empty tank can be filled by pipe A alone in 3 hours or by pipe B alone in 6 hours. A drain can empty the full tank in 4 hours. At noon, pipe A is opened. At 1:00 p.m., pipe B and the drain are both opened as well. If all three remain open, at what time will the tank be full?

(A) 2:40 p.m. (B) 3:00 p.m. (C) 3:20 p.m. (D) 3:40 p.m. (E) 4:00 p.m.

**Solution.** Phase 1 (noon to 1:00): A alone fills $\tfrac13$ of the tank.

Phase 2: net rate $\tfrac13 + \tfrac16 - \tfrac14 = \tfrac{4 + 2 - 3}{12} = \tfrac14$ tank per hour. The remaining $\tfrac23$ takes $\tfrac23 \div \tfrac14 = \tfrac83$ hours $= 2$ hours 40 minutes.

The tank is full at $1{:}00 + 2{:}40 =$ **3:40 p.m.**, choice **(D)**.

Choice (A), 2:40, adds the phase-2 duration to noon instead of to 1:00 p.m. Choice (E) assumes all three pipes run the whole time from noon (4 hours at net rate $\tfrac14$). Write the phases down and these traps disappear.

## Practice

**1.** *(Easy)* Two trains start 330 miles apart and travel toward each other on parallel tracks, one at 50 miles per hour and the other at 60 miles per hour. How many hours after they start do they meet?

(A) 2.5 (B) 3 (C) 3.5 (D) 4 (E) 6.6

<details>
<summary>Answer</summary>

**(B) 3.** Moving toward each other, the gap closes at $50 + 60 = 110$ mph, so they meet after $330 / 110 = 3$ hours. Choice (E) uses $330/50$, the time for the slower train to cover the whole distance alone.

</details>

**2.** *(Easy)* A printer prints 45 pages per minute. How many hours does it take to print 8,100 pages?

(A) 1.8 (B) 2.5 (C) 3 (D) 18 (E) 180

<details>
<summary>Answer</summary>

**(C) 3.** $8{,}100 / 45 = 180$ minutes $= 3$ hours. Choice (E) is the answer in minutes: the question asked for hours.

</details>

**3.** *(Medium)* Ana can paint a room in 5 hours. Ana and Bob, working together at their constant rates, can paint the same room in 3 hours. How many hours would Bob take to paint the room alone?

(A) 2 (B) 4 (C) 7.5 (D) 8 (E) 15

<details>
<summary>Answer</summary>

**(C) 7.5.** Bob's rate is the combined rate minus Ana's: $\tfrac13 - \tfrac15 = \tfrac{2}{15}$ room per hour, so he takes $\tfrac{15}{2} = 7.5$ hours. Choice (A), $5 - 3$, subtracts times instead of rates. Sanity check: Bob must take longer than 3 hours, and since together they take more than half of Ana's 5 hours, Bob is slower than Ana.

</details>

**4.** *(Medium)* A boat travels 36 kilometres downstream in 2 hours and returns the same 36 kilometres upstream in 3 hours. If the speed of the current is constant, what is the speed of the boat in still water, in kilometres per hour?

(A) 3 (B) 12 (C) 14.4 (D) 15 (E) 18

<details>
<summary>Answer</summary>

**(D) 15.** Downstream speed $b + c = 36/2 = 18$; upstream speed $b - c = 36/3 = 12$. Adding, $2b = 30$, so $b = 15$ (and the current is $c = 3$). Choice (C), $72/5 = 14.4$, is the average speed for the round trip, which is a different quantity; (A) is the current.

</details>

**5.** *(Medium)* Six identical machines, working at the same constant rate, produce 720 bolts in 4 hours. At this rate, how many hours would 9 such machines take to produce 1,620 bolts?

(A) 3 (B) 4 (C) 4.5 (D) 6 (E) 9

<details>
<summary>Answer</summary>

**(D) 6.** One machine makes $\tfrac{720}{6 \times 4} = 30$ bolts per hour, so 9 machines make 270 per hour, and 1,620 bolts take $1620 / 270 = 6$ hours.

Proportional check: 1,620 is 2.25 times 720 (more time), and 9 machines is 1.5 times 6 (less time): $4 \times \tfrac{2.25}{1.5} = 6$. ✓

</details>

**6.** *(Medium)* A driver travels for 3 hours at 60 miles per hour, then travels another 90 miles at 45 miles per hour. What is her average speed for the whole journey, in miles per hour?

(A) 50 (B) 52.5 (C) 53 (D) 54 (E) 56

<details>
<summary>Answer</summary>

**(D) 54.** Distance: $180 + 90 = 270$ miles. Time: $3 + 90/45 = 5$ hours. Average speed $270 / 5 = 54$ mph. Choice (B) is the mean of 60 and 45. The answer is above 52.5 because more time (3 hours versus 2) was spent at the faster speed.

</details>

**7.** *(Hard)* A runner jogs along a trail from the car park to a lake at 10 kilometres per hour and returns along the same trail. At what speed, in kilometres per hour, must she return so that her average speed for the round trip is 12 kilometres per hour?

(A) 14 (B) 15 (C) 16 (D) 18 (E) 20

<details>
<summary>Answer</summary>

**(B) 15.** Equal distances, so the average is the harmonic mean: $\tfrac{2}{\frac1{10} + \frac1v} = 12$, so $\tfrac1{10} + \tfrac1v = \tfrac16$ and $\tfrac1v = \tfrac16 - \tfrac1{10} = \tfrac{1}{15}$. She needs 15 km/h.

**Pick a distance.** Let the trail be 30 km. The round trip of 60 km at 12 km/h must take 5 hours; the way out took 3, so the way back takes 2 hours: $30 / 2 = 15$ km/h. Choice (A) is the trap "the average of 10 and 14 is 12".

</details>

**8.** *(Hard)* Machine A, working alone at its constant rate, can complete an order in 12 hours. Machine B, working alone at its constant rate, can complete the same order in 8 hours. Machine A starts the order at 8:00 a.m. Machine B joins it later, and the two machines finish the order together at 1:00 p.m. At what time did machine B start?

(A) 8:20 a.m. (B) 8:40 a.m. (C) 9:00 a.m. (D) 9:20 a.m. (E) 10:00 a.m.

<details>
<summary>Answer</summary>

**(A) 8:20 a.m.** A works all 5 hours and does $\tfrac{5}{12}$ of the order. B does the remaining $\tfrac{7}{12}$, which takes $\tfrac{7}{12} \times 8 = \tfrac{14}{3}$ hours $= 4$ hours 40 minutes. Counting back from 1:00 p.m., B started at 8:20 a.m.

Check: $\tfrac{5}{12} + \tfrac{14/3}{8} = \tfrac{5}{12} + \tfrac{7}{12} = 1$. ✓

</details>

**9.** *(Hard)* Two runners start from the same point on a 400-metre circular track at the same moment and run in opposite directions, one at 3 metres per second and the other at 5 metres per second. How many times do they pass each other during the first 9 minutes (not counting the start)?

(A) 9 (B) 10 (C) 11 (D) 12 (E) 18

<details>
<summary>Answer</summary>

**(B) 10.** Running in opposite directions, their combined distance grows at $3 + 5 = 8$ m/s, and they meet each time it grows by one lap of 400 m: every $400 / 8 = 50$ seconds. In 9 minutes $= 540$ seconds they meet at 50, 100, ..., 500 seconds, which is $\lfloor 540 / 50 \rfloor = 10$ times. Choice (D) would be the count for 10 minutes. (Had they run in the same direction, the gap would grow at only 2 m/s, and they would meet just twice, every 200 seconds.)

</details>

**10.** *(Medium)* An inlet pipe can fill an empty tank in 5 hours. When the drain at the bottom of the tank is also open, the inlet takes 20 hours to fill the empty tank. If the tank is full and the inlet is closed, how many hours does the drain take to empty it?

(A) 4 (B) $6\tfrac23$ (C) 10 (D) 15 (E) 25

<details>
<summary>Answer</summary>

**(B) $6\tfrac23$.** Net rate $= \text{inlet} - \text{drain}$: $\tfrac1{20} = \tfrac15 - \tfrac1d$, so $\tfrac1d = \tfrac15 - \tfrac1{20} = \tfrac{3}{20}$ and $d = \tfrac{20}{3} = 6\tfrac23$ hours. Choice (D), $20 - 5$, subtracts times. Sanity check: the drain ($6\tfrac23$ h) is slower than the inlet (5 h), as it must be for the tank to fill at all. ✓

</details>

**11.** *(Medium, Data Sufficiency)* Cars X and Y each travel the same 120-mile route at constant speeds. How many minutes less than car Y does car X take?

(1) Car X's speed is 1.25 times car Y's speed.
(2) Car X's speed is 12 miles per hour greater than car Y's speed.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(C).** The time difference is $\tfrac{120}{y} - \tfrac{120}{x}$ hours, which depends on the actual speeds.

(1) alone: X takes $\tfrac{1}{1.25} = 80\%$ of Y's time, so X saves 20% of Y's time; but Y's time is unknown (at $y = 40$ X saves 36 minutes, at $y = 60$ it saves 24 minutes). Not sufficient.

(2) alone: $y = 48$ gives 30 minutes saved; $y = 60$ gives 20 minutes. Not sufficient.

Together: $1.25y = y + 12$, so $y = 48$ and $x = 60$. Times are 2.5 hours and 2 hours: X takes 30 minutes less. Sufficient.

</details>

**12.** *(Hard, Data Sufficiency)* Dana drove from her home to a conference. Was her average speed for the whole drive greater than 50 miles per hour?

(1) She drove the first half of the distance at an average speed of 40 miles per hour.
(2) She drove the second half of the distance at an average speed of 65 miles per hour.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(C).** Each statement alone leaves the other half's speed free: with (1), a second half at 40 mph gives an average of 40 (no), and a second half at 200 mph gives $\tfrac{2 \cdot 40 \cdot 200}{240} \approx 66.7$ (yes). Similarly for (2). Neither is sufficient.

Together, the halves are equal distances, so the average is the harmonic mean:

$$
\frac{2 \cdot 40 \cdot 65}{40 + 65} = \frac{5200}{105} \approx 49.5 < 50.
$$

The answer to the question is a definite **no**, which is sufficient. The trap is to compute the ordinary average, $52.5$, and answer "yes". Either way the choice is (C), but on a Problem Solving version of this question the trap would cost you the point.

</details>

## Takeaways

- Everything is $\text{amount} = \text{rate} \times \text{time}$; write units next to every number.
- Use a table with one row per mover or leg; the sentences link the rows.
- Average speed is total distance over total time. For equal distances it is the harmonic mean $\tfrac{2ab}{a+b}$, below the ordinary mean.
- Relative speed: add rates when closing head-on, subtract when chasing; the gap to close in a chase is the head start.
- Work rates add (drains subtract); times never add. For two workers, $t = \tfrac{ab}{a+b}$.
- For workers who start or stop at different times, sum each worker's rate × time worked to 1 job.
- Production problems: find the rate of one machine per hour, then scale; pick numbers when the problem uses only letters.

## Further reading

- GMAC, *GMAT Official Guide* (current edition), for official rate and work questions; time yourself and note which trap each wrong choice represents.
- [Translating words into equations](../translating-words-into-equations/) for setting up the equations, and [Ratios](../../arithmetic/ratios/) for the proportional reasoning behind production problems.
- The harmonic mean appears again as a weighted average in [Mixtures and interest](../mixtures-and-interest/).
