gsap.from('.logo', .8, {
    opacity: 0,
    x: -20,
    ease: Expo.easeInOut
})

gsap.timeline()
    // .to('.overlay', .5, { delay: 1, left: '-100%', ease: Expo.easeInOut, stagger: 0.5 }, "-0.5")
    .from(".heroContents", { opacity: 0, scale: 0, ease: "back" },)
    .from('.heroImage', { x: '120%', ease: Power4.easeInOut }, "-=.2");