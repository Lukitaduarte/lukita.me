---
title: Why did we choose to migrate from native to Flutter?
description: How Youse's mobile team decided to replace native development with Flutter, and what we learned along the way.
date: 2022-03-30 18:27:24 -0300
categories: [Engineering, Mobile]
tags: [flutter, mobile, youse, architecture]
lang: en
image:
  path: /assets/img/posts/flutter/01.jpeg
  alt: Why did we choose to migrate from native to Flutter?
---

[Leia em português](/posts/por-que-migrar-de-nativo-para-flutter/){: .lang-link}

> This article is an English translation of the original article written in Portuguese, first published on [Youse Tech, on Medium](https://medium.com/youse-tech/por-que-optamos-migrar-de-nativo-para-o-flutter-3dc921612efb), on March 30, 2022.
{: .prompt-info }

It's no secret to any IT manager that every developer will always want to build solutions that are robust, scalable and failure-proof from an engineering standpoint. But at the same time, when we look at it from a product perspective, that solution needs to be innovative, simple and intuitive for the user. The final product is the result of walking the fine line between those pillars.

Along the journey of building a product, we fairly often run into situations that demand hard choices, choices that will shape our solution in the long run and that will certainly cost considerable effort when made the wrong way.

In 2020, shortly before what would become one of the saddest and most challenging episodes for humanity since the Second World War, the Covid-19 pandemic, we on Youse's mobile team found ourselves in a scenario that has become common in today's tech market: a shortage of professionals. After yet another strong push from the market took away a relevant share of our talent, we were once again down to practically one Android and one iOS developer.

With valuable knowledge and almost 4 years of experience building our app in the hands of very few people, and documentation that was quite lacking at the time, a first trigger went off, one that led to the decision you already saw in the title.

Our team, once made up of 10 native developers, five of them iOS and the other five Android, had managed over that period to build a robust application with amazing features. But Youse couldn't stop there, right?

As the first insurtech in Brazil, Youse was driven by innovation from day one. That determination and pioneering spirit gave us a considerable advantage over the big insurers, and even over the more recent digital ones.

But, just like us, the market was going full steam, and doing very well! Our initial advantage was getting smaller and smaller. We needed to keep innovating, building new features (even more amazing than the previous ones) and developing new products that met our customers' needs and added value to their day-to-day.

It's no secret to any mobile developer that native development is verbose, with a long learning path before you reach a comfortable proficiency. Building smooth, high-performance features is a challenge even for the most experienced! And with the shortage of experienced (and increasingly expensive) native professionals, how do you parallelize training and mentoring juniors with the delivery speed companies demand? That was our second trigger…

On top of the challenge of growing a professional in native technology, there were other points weighing negatively in Youse's context. At the end of 2019, CARGO, our design system, was starting to take shape. With it, some of the challenges we'd faced in the past came back: we'd have to refactor our entire UI, at least one more time, to match CARGO's new behaviors and specs; once again we'd need slightly (sometimes not so slightly) different specs per platform to follow each one's guidelines…

For a while, our teams no longer had an even number of developers per platform, and features shipped with weeks (sometimes even months) of delay between platforms. Those features often had considerable differences in behavior and look. That was our third trigger…

What used to be Youse's golden goose, our app, the main differentiator against any other insurer, was becoming a bottleneck. Something had to be done…

**And we did it!**

Once the whole chapter agreed that we needed to change, we had to define those changes: what were the pains of the product team and of us, the developers? From there, we came up with a few premises to guide our decision and solve the triggers above. Those premises were:

- A cross-platform technology that enables accelerated development speed and a unified experience across platforms;
- Performance as close as possible to native;
- A low barrier to entry and a gentle learning curve for developers from other stacks;
- Community.

Back in November 2019, we started looking for technologies that met those premises. React Native quickly came to the table: the mobile team had just merged with the web team to form the frontend chapter, there were people proficient in React, and some of the mobile team had experience with the technology from past projects. The initial barrier was practically gone, and the React community needs no introduction, right?

But it was precisely those previous experiences with React Native, shared with the team through stories of a painful initial setup, heavy dependence on third-party libraries, noticeably worse performance than native, plus strong rejection from native developers due to the barrier of moving from native code to JavaScript, that made us quickly give up on that option.

Kotlin Native was still a question mark back then and didn't meet the cross-platform premise the way we wanted. As soon as the previous technologies were ruled out, Flutter was already standing out, not only among us but worldwide. Companies like Nubank in Brazil, and many others abroad, were already announcing decisions similar to the one we were looking for, with Flutter as the star.

![Chart comparing Google searches for Flutter, Kotlin and React Native. In September 2019, when we started our internal studies, Flutter took the lead.](/assets/img/posts/flutter/02.png)
_Chart comparing Google searches for Flutter, Kotlin and React Native. In September 2019, when we started our internal studies, Flutter took the lead._

So we quickly started studying Flutter. Complete courses were made available to the team, and dojos, talks and syncs were held weekly to discuss what we'd learned and move forward in the Flutter ecosystem. The team adapted very quickly and the development speed was impressive. The performance difference was practically imperceptible, even to the sharpest eyes, and although the community was still maturing, it was growing fast, so it wasn't hard to decide we needed to see, in practice, how Flutter would behave.

In January, we shipped our first Flutter feature, MGM (Invite Friends and Earn): a simple feature, yet enough for Flutter to show all its power. Integrating it with our native app was extremely easy, the transition between Flutter and native was smooth, and not even our most optimistic predictions expected such a satisfying result.

![Our first Flutter feature in production, initially as a proof of concept and experiment. Today it has already been refactored following our new standards.](/assets/img/posts/flutter/03.gif)
_Our first Flutter feature in production, initially as a proof of concept and experiment. Today it has already been refactored following our new standards._

Remember when I mentioned, in the first paragraphs, situations that challenge us to make hard decisions that will shape the future of our product? Well, sometimes they're not that hard…

After our first Flutter feature launched successfully, we started encouraging team members to build their next deliveries with it. But we quickly realized this wasn't a good idea: it didn't come as naturally as we'd imagined…

Hold on, didn't Flutter meet all our premises? So what was going wrong? The team seemed so engaged in studying and excited about the technology's potential… Why didn't the team embrace it right away?

The answer was so obvious and simple that nobody had thought of it: we were all native developers! No matter how excited we were about Flutter, our comfort zone for shipping a new feature would always be native, if we had the choice! So, after that one-month period in which only a few chose to use Flutter, we sat down, discussed it and decided…

**From now on, it's Flutter, period!**

From March onward, it was decided that every new feature would be built in Flutter, in a gradual migration that didn't stop our delivery pipeline, a process that continues to this day, a year and a half later. I'm writing this article with the migration close to the end. We faced countless challenges: from creating an initial modular, multi-package architecture that allowed an easy, decoupled gradual migration, to a standardized and robust state management architecture, building a design system with a unified experience, and broad test coverage.

All of this with a team that is now half the size it was 2 years ago, but with a development speed that is, if not close, even faster! The final verdict couldn't have been any different. Our decision proved positive, with a great outlook for the future: one year into Flutter, and with the process still in transition, we're already reaping results that make us believe it was the right call.

You, a developer about to start a project, or working at a company in a scenario like ours, feeling the same pains I described, are probably asking yourself right now: should I follow the same path?

The obvious answer is: I don't know! I believe every case is different, every project is different, but I can say with certainty that Flutter is a robust, mature-enough solution, with absurd development speed and the ease of learning any tech company needs today. If I could give you one tip, it would be: consider Flutter, look into it, it will probably meet your needs and save you precious time.

Finally, in this article I described my experience as a native developer who led this internal change. It was only possible with the help of an engaged, multidisciplinary team, and a company and leadership committed to the team, giving us full autonomy in decision-making.

If you want to know more about the challenges we faced or the development decisions we made, feel free to comment and ask anything!

If you're interested in joining this journey with us, we have open positions and a whole world of post-migration challenges and features to explore.

Jobs (2022 posting): [https://jobs.kenoby.com/vagas-youse/job/dev-mobileflutter/6102ba438f605b6168853b77](https://jobs.kenoby.com/vagas-youse/job/dev-mobileflutter/6102ba438f605b6168853b77?utm_source=website)
