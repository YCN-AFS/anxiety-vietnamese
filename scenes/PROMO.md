# intro

`SceneSetup.intro();`

# intro-play-button

(...51)

[PLAY!](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`

# intro-start

(...500)

`clearText()`

n3: Vậy trước khi bắt đầu, *cậu* muốn đọc như thế nào?

`publish("show_options_bottom")`

# intro-start-2

n3: Bây giờ, chúng ta hãy bắt đầu câu chuyện của mình...

```
publish("hide_tabs");
clearText();
```

(...1000)

`publish("intro-to-game-2")`

n2: ĐÂY LÀ MỘT CON NGƯỜI

(...600)

`clearText()`

(...300)

`publish("intro-to-game-3")`

# act1

```
SceneSetup.act1();
publish("hide_tabs");
music('battle', {volume:0.5});
```

(...300)

n: VÀ ĐÂY LÀ SỰ LO ÂU CỦA CON NGƯỜI

n: _BẠN_ LÀ SỰ LO ÂU

(#act1_normal)


# act1_normal

```
hong({body:"putaway"});
sfx("rustle");
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Nope. No, nope, not listening. Gonna check my phone.

```
sfx("rustle2");
hong({body:"phone1", mouth:"neutral", eyes:"neutral"})
```

n: YOUR JOB IS TO PROTECT YOUR HUMAN FROM *DANGER*

`bb({eyes:"look", mouth:"small_lock", body:"fear"})`

b: Gasp! You're scrolling your life away on Twitter! Again!

```
bb({eyes:"normal", mouth:"normal", body:"normal"});
hong({eyes:"annoyed"});
```

h: Yeah I wonder why I don't just sit and listen to my thoughts more often.

`hong({eyes:"neutral"});`

n: QUICK, WARN THEM ABOUT A *DANGER!*

```
bb({eyes:"look"});
```

[Oh no, look at that horrible news story!](#act1d_news)

[Oh no, is that tweet secretly about *us?*](#act1d_subtweet)

[Hãy một GIF về một con mèo đang uống sữa.](#act1d_milk)

# act1d_milk

`hong({mouth:"smile", eyes:"surprise"});`

h: Heh, đúng rồi, dễ thương quá, tớ--

```
hong({mouth:"shock", eyes:"shock"});
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.8;
```

b: MÈO KHÔNG THỂ TIÊU HÓA SỮA VÀ CẬU LÀ NGƯỜI TỒI TỆ VÌ THÍCH LÀM ĐAU ĐỘNG VẬT!

(...200)

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
attack("20p", "bad");
publish("hp_show");
```



