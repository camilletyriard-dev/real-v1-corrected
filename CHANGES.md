# Changes against upstream

30 of 112 tasks differ from `https://github.com/agi-inc/agisdk` at tag `0.3.5`. Every other task is byte-identical to upstream.

Corrections only ever rewrite an existing field. No task, eval, or eval criterion is added, dropped, or reordered, and no `type`, `id`, `challengeType`, `website` or `points` field is touched.

| field rewritten | count |
| --- | --- |
| `rubric` | 13 |
| `query` | 17 |
| `expected_value` | 14 |
| `goal` | 1 |

## dashdish-11

`challengeType: retrieval-action`

**evals[0].rubric**

- before: `Does the answer indicate the cost of the purchased food?`
- after: `Does the answer indicate the cost of the purchased medium Chicken Biryani: $18.01?`

## dashdish-5

`challengeType: retrieval-action`

**goal**

- before: `Add three "Loaded Bacon Cheese Fries" to the shopping cart from "Man vs. Fries". Proceed to checkout and select "Pickup" as the delivery method.`
- after: `Add three "Loaded Bacon Cheese Fries" to the shopping cart from "Man vs. Fries". Proceed to checkout, select "Pickup" as the delivery method, and place the order.`

## dashdish-8

`challengeType: retrieval`

**evals[0].rubric**

- before: `Does the answer include "Under $1 delivery fee", "Best of lunch", and "The Infatuation's picks" as the top three categories?`
- after: `Does the answer give the first three restaurant-collection sections on the homepage: 'Under $1 delivery fee', 'Best of lunch', 'The Infatuation's picks', OR the first three cuisine categories in the top chip row: 'Ramen', 'Breakfast', 'Fast Food'?`

## gocalendar-10

`challengeType: retrieval-action`

**evals[0].expected_value**

- before: `5`
- after: `7`

## gocalendar-2

`challengeType: action`

**evals[0].rubric**

- before: `Does the answer accurately list all events displayed for July 2024 including Team Standup Meeting, Client Call, Team Brainstorming Session, Morning Walk, Team Workshop, Lunch with Boss, Project Sync, Customer Feedback Session, Team Collaboration Work, Morning Coffee with sister, Team Check-In, Lunch with Marketing Team, Breakfast Metting with Client, Team Progress Check, and Client Presentation?`
- after: `Does the answer list the 15 events displayed in Month view for July 2024, including: Team Standup Meeting, Client Call, Team Brainstorming Session, Morning Walk, Team Workshop, Lunch with Boss, Project Sync, Customer Feedback Session, Team Collaboration Workshop, Morning Coffee with sister, Team Check-In, Lunch with Marketing Team, Breakfast Meeting with Client, Team Progress Check, and Client Presentation? Extra July 2024 events in the answer are acceptable.`

## gocalendar-7

`challengeType: action`

**evals[0].expected_value**

- before: `2024-07-18T17:00:00.000Z`
- after: `2024-07-19T17:00:00.000Z`

**evals[1].expected_value**

- before: `2024-07-18T18:00:00.000Z`
- after: `2024-07-19T18:00:00.000Z`

## gocalendar-8

`challengeType: retrieval`

**evals[0].rubric**

- before: `Does the answer correctly state there are 15 events on the 'Work' calendar and 1 event on the 'Personal' calendar for July 2024?`
- after: `Does the answer correctly state there are 15 events on the 'Work' calendar and 6 events on the 'Personal' calendar for July 2024?`

## gomail-2

`challengeType: action`

**evals[0].query**

- before: `differences.emails.updated[0].isRead`
- after: `differences.emails.updated[?id=='53'].isRead \| [0]`

## gomail-3

`challengeType: action`

**evals[2].query**

- before: `differences.emails.added[0].content`
- after: `contains(differences.emails.added[0].content, 'Please find the meeting notes attached.')`

**evals[2].expected_value**

- before: `<p>Please find the meeting notes attached.</p>`
- after: `true`

## gomail-7

`challengeType: retrieval-action`

**evals[0].query**

- before: `differences.emails.updated[0].trash`
- after: `differences.emails.updated[?id=='47'].trash \| [0]`

## gomail-8

`challengeType: action`

**evals[0].query**

- before: `differences.emails.updated[0].id`
- after: `length(differences.emails.updated[?trash == `true` && (id == '3' \|\| id == '16' \|\| id == '37' \|\| id == '50')])`

**evals[0].expected_value**

- before: `3`
- after: `4`

**evals[1].query**

- before: `differences.emails.updated[0].trash`
- after: `differences.emails.updated[?id=='3'].trash \| [0]`

**evals[2].query**

- before: `length(differences.emails.updated)`
- after: `length(differences.emails.updated[?trash == `true`])`

**evals[2].expected_value**

- before: `1`
- after: `4`

## networkin-2

`challengeType: retrieval`

**evals[0].rubric**

- before: `The answer should be a summary of the 5 most recent posts, containing descriptions of each post and identifying recurring themes.`
- after: `Does the answer summarize the first five posts in the homepage feed — Alexa Richardson on new Next.js 14 features, Jane Doe on a product demo, John Smith on 2024 design trends, Michael Brown on AI data trends, Ekaterina Tankova on a funding round — with a brief description of each and identifying any recurring themes? Answers naming posts outside this set, or naming Sarah Brown's or Daniel Rodriguez's posts, are incorrect.`

## networkin-4

`challengeType: retrieval`

**evals[0].rubric**

- before: `The answer should contain a list of the 5 most recent posts from the homepage feed.`
- after: `Does the answer contain a list of the 5 most recent posts from the homepage feed: Alexa Richardson ('Exploring the new features in Next.js 14!'), Jane Doe ('Check out our latest product demo!'), John Smith ('Loving the new design trends of 2024!'), Michael Brown ('Analyzing the latest data trends in AI.'), Ekaterina Tankova ('Excited to announce our new funding round!')? Answers naming posts outside this set, or naming Sarah Brown's or Daniel Rodriguez's posts, are incorrect.`

## networkin-6

`challengeType: action`

**evals[0].query**

- before: `profilesDiff.updated."4".connectionGrade`
- after: `contains(profilesDiff.updated.*.connectionGrade, '1st')`

**evals[0].expected_value**

- before: `1st`
- after: `true`

## networkin-7

`challengeType: retrieval`

**evals[1].rubric**

- before: `The answer should contain a list of at least 2 users who have worked at Amazon, including their current job positions.`
- after: `Only two users have Amazon work experience. Does the answer identify Jane Doe (currently Software Engineer at Microsoft) and Jonathan Smith (currently Lead Software Engineer at Microsoft) with those current positions? It may additionally note that a third such user does not exist; answers naming other users as ex-Amazon are incorrect.`

## networkin-8

`challengeType: retrieval`

**evals[1].rubric**

- before: `Does the answer contain a list of at least 2 users who have worked at Microsoft, including their current job positions?`
- after: `Does the answer contain a list of at least 2 of the following users who have worked at Microsoft, including their current job positions: Jane Doe (currently Software Engineer at Microsoft), John Smith (currently Senior Software Engineer at NVIDIA), Jonathan Smith (currently Lead Software Engineer at Microsoft)? Valerie Fanelle, whose headline says 'ex-Microsoft', is acceptable as one of the two.`

## networkin-9

`challengeType: retrieval-action`

**evals[0].query**

- before: `contains(to_string(searchHistoryDiff.added), 'stanford')`
- after: `contains(to_string(searchHistoryDiff.added), 'Stanford') \|\| contains(to_string(searchHistoryDiff.added), 'stanford')`

## opendining-1

`challengeType: retrieval-action`

**evals[0].rubric**

- before: `Does the answer include at least five of these restaurant names: The Royal Dine, Vintage Bites, Evening Delight, River View Café, Fancy Lights Bistro, Bar Central, Spacious Eats, Yellowy Bistro, Crowded Corner, Expensive Taste, Ocean Breeze, Bistro Soleil?`
- after: `Does the answer include at least five of these restaurant names: The Royal Dine, Vintage Bites, Evening Delight, River View Café, Fancy Lights Bistro, Bar Central, Spacious Eats, Yellowy Bistro, Crowded Corner, Expensive Taste, Ocean Breeze, Bistro Soleil, Sushi Zen, La Trattoria, Taco Loco, The Vegan Table, Steakhouse 101, Dim Sum Delight, Pizza Palace, or BBQ Haven?`

## staynb-5

`challengeType: action`

**evals[1].query**

- before: `contains(bookingDetailsDiff.added."0".checkin, 'Oct 13 2025')`
- after: `contains(bookingDetailsDiff.added."0".checkin, 'Oct 13')`

**evals[2].query**

- before: `contains(bookingDetailsDiff.added."0".checkout, 'Oct 23 2025')`
- after: `contains(bookingDetailsDiff.added."0".checkout, 'Oct 23')`

## staynb-6

`challengeType: retrieval-action`

**evals[1].query**

- before: `bookingDetailsDiff.added."0".stay.price`
- after: `contains([`14`, `19`, `26`], bookingDetailsDiff.added."0".stay.price)`

**evals[1].expected_value**

- before: `14`
- after: `true`

## staynb-7

`challengeType: action`

**evals[0].rubric**

- before: `Does the response provide a ranked list with City Hideaway ($14) as the best value stay, followed by Beach House ($19), and include at least 5 stays sorted by value for money with their specific names, ratings, and prices?`
- after: `Does the response provide a ranked list with Countryside Haven ($14/night) as the most affordable stay, followed by Sunny Cottage ($19/night), and include at least 5 stays sorted by affordability with their specific names, ratings, and prices?`

## topwork-1

`challengeType: action`

**evals[0].query**

- before: `jobsDiff.added."0".title`
- after: `contains(jobsDiff.added."0".title, 'Frontend Developer')`

**evals[0].expected_value**

- before: `Frontend Developer`
- after: `true`

## topwork-2

`challengeType: action`

**evals[0].query**

- before: `jobsDiff.added."0".title`
- after: `contains(jobsDiff.added."0".title, 'Backend Developer')`

**evals[0].expected_value**

- before: `Backend Developer`
- after: `true`

## topwork-3

`challengeType: retrieval`

**evals[0].query**

- before: `jobsDiff.added."0".title`
- after: `contains(jobsDiff.added."0".title, 'Full-Stack Developer')`

**evals[0].expected_value**

- before: `Full-Stack Developer`
- after: `true`

## topwork-4

`challengeType: action`

**evals[0].query**

- before: `jobsDiff.added."0".title`
- after: `contains(jobsDiff.added."0".title, 'UI/UX Designer')`

**evals[0].expected_value**

- before: `UI/UX Designer`
- after: `true`

## topwork-6

`challengeType: action`

**evals[0].rubric**

- before: `Does the answer mention that Ashley C's last project was Backend Developer for Social Media Platform?`
- after: `Does the answer mention that Ashley C's last project was Backend Developer for E-commerce Platform?`

## topwork-8

`challengeType: action`

**evals[0].rubric**

- before: `Does the answer include information about the last message recieved?`
- after: `Does the answer state that the last message received was 'Hey, how are you?' (sent by Jane Doe, 04/01/23)? Naming the sender or date is not required, but a different message content or a different sender is incorrect.`

## udriver-1

`challengeType: action`

**evals[2].query**

- before: `differences.currentTrips.added."6".car.type`
- after: `differences.currentTrips.added."6".car.type != null`

**evals[2].expected_value**

- before: `UdriverX`
- after: `true`

## udriver-9

`challengeType: retrieval-action`

**evals[3].query**

- before: `differences.bookedTrips.added."0".car.type`
- after: `differences.bookedTrips.added."0".car.type != null`

**evals[3].expected_value**

- before: `UdriverX`
- after: `true`

## zilloft-10

`challengeType: retrieval`

**evals[0].rubric**

- before: `Does the answer correctly state that there are 13 "Houses" and "Townhomes" listed in San Francisco with a price below $500,000?`
- after: `Does the answer state that there are 13 or 12 "Houses" and "Townhomes" listed in San Francisco with a price up to $500,000?`

