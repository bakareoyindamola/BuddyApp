gsap.from('.logo', .8, {
    opacity: 0,
    x: -20,
    ease: Expo.easeInOut
})

gsap.timeline()
    .from(".heroContents", { opacity: 0, scale: 0, ease: "back" })