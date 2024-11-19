# act4

```
SceneSetup.act4();
publish("SAVE_GAME", ["act4"]);
Game.FORCE_CANT_SKIP = true;
```

(...5001)

```
publish("set_how_many_prompts", [1]);
Game.FORCE_CANT_SKIP = false;
Game.CLICK_TO_ADVANCE = true;
```

n3: (game auto-saved)

```
Game.clearText();
Game.FORCE_CANT_SKIP = true;
```

(...1001)

```
var hong_frame = _.INJURED ? 9 : 0;
publish("act4", ["hong_walks_in",hong_frame]);
sfx("grass_step1", {volume:0.1});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.2});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.25});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.3});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.35});
```

(...1667)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.35});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.35});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.35});
```

(...1333)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.20});
```

(...167)

```
publish("act4_hong_sits");
```

(...66)

```
publish("act4", ["hong_transition", "next"]);
sfx("squeak");
```

(...133)

`publish("act4", ["hong_transition", "next"]);`

(...1333)

```
publish("act4", ["hong_transition", "next"]);
sfx("rustle");
```

(...333)

`publish("act4", ["hong_transition", "next"]);`

(...1001)

```
publish("act4", ["hong_transition", "next"]);
```

(...333)

```
publish("act4", ["hong_transition", 9]);
sfx("sandwich");
```

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", 9]);`

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", 9]);`

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", "next"]);`

(...1466)

`publish("act4-out-1");`

(...201)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

```
publish("act4-show-chars");
Game.FORCE_CANT_SKIP = false;
```

(...901)

`hong({body:"sigh_1"})`

(...601)

```
hong({body:"sigh_2"});
bb({eyes:"look_down"});
```

h: *thở dài*

```
hong({body:"hold", eyes:"normal", mouth:"normal"});
bb({eyes:"normal"});
```

h: Vậy bài học rút ra từ câu chuyện ^ngu xuẩn^ này là gì?

`hong({body:"one_up", eyes:"annoyed"})`

h: ‘Chúng ta đã  rút ra được *bài học* gì? Mình *thật là* ngu ngốc, những “người bạn” thì *đang cố* lợi dụng mình và chúng ta suýt nữa thì *chết*.

`hong({body:"normal", eyes:"normal"})`

{{if _.INJURED}}
[Đúng thế, còn chưa kể tiền viện phí.](#act4a_bill)
{{/if}}

{{if !_.INJURED}}
[r: Ừ, và chưa kể đến tổn thương gan nữa.](#act4a_liver)
{{/if}}

[Phải rồi, đó *là* trường hợp xấu nhất.](#act4a_worst)

[Yep, như mình cảnh báo.](#act4a_right)

# act4a_bill

`hong({eyes:"annoyed_l", mouth:"narrow"});`

h: Đúng vậy. Tớ nghĩ rằng  bảo hiểm của sẽ không chi trả cho việc "làm một con ngốc."

`hong({eyes:"annoyed", mouth:"normal"});`

b: Và rồi... chúng ta vẫn sống sót!

`hong({eyes:"normal"});`

h: ?

(#act4b)

# act4a_liver

`bb({eyes:"normal_d"});`

b: Chắc chắn là chúng ta đã rút ngắn vài năm tuổi thọ của mình...

`bb({eyes:"surprise"});`

b: Nhưng ít nhất chúng ta *vẫn còn* có tuổi thọ! Chúng ta đã sống sót!

```
hong({eyes:"surprise"});
bb({eyes:"normal"});
```

h: ?

(#act4b)

# act4a_worst

`bb({eyes:"normal_d"});`

b: Nhưng mà...

h: Hm?

`bb({eyes:"surprise"});`

b: Chúng ta đã sống sót!

(#act4b)

# act4a_right

`bb({eyes:"normal_d"});`

b: Nhưng... cậu cũng đúng.

`hong({eyes:"surprise"});`

h: Hm?

`bb({eyes:"normal"});`

b: Mình *đúng là* con sói kêu cứu (truyện cậu bé chăn cừu). 

b: Nên khi mối nguy thực sự đến, – như một lẽ đương nhiên–  cậu đã không tin mình.

`bb({eyes:"surprise_r"});`

b: Nhưng chúng ta vẫn sống sót!

(#act4b)

# act4b

```
bb({eyes:"normal", mouth:"normal"});
hong({eyes:"normal", mouth:"normal"});
```

b: Dù thế nào đi nữa, chúng ta vẫn ở đây.

`hong({eyes:"suspect"});`

{{if _.INJURED}}
h: Cậu có vẻ khá bình tĩnh dù chúng ta vừa trải qua một trải nghiệm cận kề cái chết.
{{/if}}

{{if !_.INJURED}}
h: Cậu có vẻ khá bình tĩnh dù chúng ta vừa trải qua một trải nghiệm *gần như* là chết.
{{/if}}

```
hong({eyes:"normal"});
bb({eyes:"annoyed_d", mouth:"narrow"});
```

b: Ờ, nó làm mọi thứ khác bớt đáng sợ hơn khi so sánh. Nó cũng khiến tớ suy nghĩ nhiều hơn.

`bb({eyes:"normal", mouth:"normal"});`

b: Nếu tớ đánh nhau với cậu mà chẳng có ích gì, vì nó không bảo vệ được cậu...

h: Nhưng tớ đánh nhau với cậu cũng tệ, vì nó chỉ làm cậu hét to hơn thôi...

`bb({eyes:"normal_r"})`

b: Vậy có lẽ...

`bb({eyes:"normal"})`

h: Có lẽ chúng ta không cần phải đánh nhau.

```
Game.FORCE_CANT_SKIP = true;
Game.clearText();
```

(...301)

`publish("smash",[0]);`

(...2001)

```
publish("smash",[1]);
sfx("smash_glass");
```

(...2601)

```
publish("smash",[2]);
bb({eyes:"normal", mouth:"normal"});
hong({eyes:"normal", mouth:"normal"});
```

(...2001)

`Game.FORCE_CANT_SKIP = false;`

(#act4b_2)

# act4b_2

```
music('dontfight',{fade:5, volume:0.6});
bb({eyes:"annoyed_d"});
```

b: Tớ không phải là Sói Gian Ác. Nhưng tớ cũng không phải là sói canh gác.

`bb({eyes:"sad_d"})`

b: Tớ là một chú chó bị tổn thương.

`bb({eyes:"sad"})`

b: Chúng mình đã trải qua những chuyện khó khăn. Có thể là chấn thương hoặc bỏ rơi. Đó là lý do mình đôi khi phản ứng thái quá và nói:

```
sfx("yaps", {volume:0.6});
bb({body:"yap_1"});
Game.FORCE_CANT_SKIP = true;
Game.WORDS_HEIGHT_BOTTOM = 215;
Game.FORCE_TEXT_DURATION = 90;
Game.FORCE_NO_VOICE = true;
```

b: GÂU GÂU GÂU GÂU GÂU 

(...1884)

```
Game.WORDS_HEIGHT_BOTTOM = -1;
Game.FORCE_CANT_SKIP = false;
bb({body:"normal", mouth:"scream", eyes:"scream_sad"});
```

b: Nhưng tớ *không muốn* trở thành một chú chó hèn nhát! Tớ muốn bảo vệ cậu! Tớ muốn trở thành một chú chó tốt!

`bb({eyes:"sad", mouth:"normal"});`

b: Cậu ơi... cậu có giúp tớ thuần hóa con sói này không?

`hong({eyes:"sad"})`

h: Tớ... tớ sẽ cố gắng.

`hong({eyes:"normal_l", body:"chin", mouth:"narrow"})`

h: Được rồi. Mối quan hệ lành mạnh với cảm xúc. Các mối quan hệ cần giao tiếp. Vậy hãy giao tiếp nào.

`hong({eyes:"normal", body:"hands_1", mouth:"normal"})`

h: Năm phút tới sẽ nghe có vẻ siêu sến, nhưng hãy giả vờ cho đến khi chúng ta làm được nhé.

```
hong({body:"hands_2", mouth:"normal"});
```

h: Gửi con sói bên trong... *cậu* đang cảm thấy như thế nào? 

n2: TỔNG SỐ NỖI SỢ ĐÃ SỬ DỤNG:

n2: *SỢ TỔN THƯƠNG* {{_.attack_harm_total}}, *SỢ KHÔNG ĐƯỢC YÊU THƯƠNG* {{_.attack_alone_total}}, *SỢ THÀNH NGƯỜI XẤU* {{_.attack_bad_total}}

n2: CẬU MUỐN NÓI VỀ NỖI SỢ NÀO TRƯỚC? (CẬU CÓ THỂ LÀM CÁC NỖI SỢ KHÁC SAU)

```
_.a4_fears_discussed = 0;
_.num_thanks = 0;
hong({body:"normal"});
bb({eyes:"normal"});
```

[Mình sợ bị tổn thương.](#act4_harm)

[Mình sợ sự cô đơn.](#act4_alone)

[Mình sợ trở thành người xấu.](#act4_bad)

# act4_harm

```
_.a4_talked_about_harm = true;
_.a4_fears_discussed += 1;
```

`bb({eyes:"normal_d"})`

b: Mình muốn bảo vệ nhu cầu an toàn về thể xác của cậu,

`bb({eyes:"sad_d"})`

b: Nhưng *cả thế giới* có vẻ thật nguy hiểm. Toàn là bi kịch và ác độc.

`bb({eyes:"sad"})`

{{if _.a4_fears_discussed==1}}
b: Tớ không biết nữa, đủ rồi việc *tớ* chọn điều gì để nói tiếp. Cậu thì sao, người?
{{/if}}

{{if _.a4_fears_discussed==2}}
b: Lần nữa, trở lại với cậu, con người ạ. Cậu nghĩ sao?
{{/if}}

{{if _.a4_fears_discussed==3}}
b: Cậu có thêm suy nghĩ gì không, con người ạ?
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Cậu nói đúng. Vậy cùng nhau bảo vệ bản thân nhé.](#act4_harm_skills)

[Vậy hãy để mình đối mặt với *nhiều* nguy hiểm hơn nhé.](#act4_harm_exposure)

[Cảm ơn cậu.](#act4_thanks) `_.thanks_for = "physical safety";`

# act4_harm_skills

`bb({eyes:"look_down", body:"paw"})`

b: Nhưng... làm thế nào đây? Mình có răng và móng vuốt, nhưng mình chỉ là một phép ẩn dụ thôi.

```
bb({ body:"normal", eyes:"normal" });
hong({ body:"one_up", eyes:"surprise" });
```

h: Chúng ta có thể học tự vệ? Tham gia một cộng đồng bảo vệ lẫn nhau? Cải thiện sức khỏe và ranh giới cá nhân của mình?

```
bb({ eyes:"annoyed_r" });
hong({ body:"normal", eyes:"normal" });
```

b: Có lẽ, nhưng...

[Chúng ta nên bắt đầu từ đâu?](#act4_harm_skills_start)

[Nếu nó không có tác dụng thì sao?](#act4_harm_skills_work)

[Nếu chúng ta quá chú trọng vào "an toàn" thì sao?](#act4_harm_skills_overboard)

# act4_harm_skills_start

`bb({ eyes:"sad_d" })`

b: Có quá nhiều việc phải làm, quá nhiều thứ chúng ta cần phải sửa đổi về bản thân mình. Chúng ta *bắt đầu* bằng điều gì?

`hong({ body:"shrug", eyes:"surprise" })`

h: Chúng ta đang bắt đầu ngay bây giờ.

`bb({ eyes:"normal", mouth:"narrow" })`

b: Eh?

```
bb({ body:"normal", mouth:"normal" });
hong({ body:"normal", mouth:"normal", eyes:"normal"});
```

h: Chúng ta đang thực hành giao tiếp tốt ngay bây giờ. Điều này sẽ giúp chúng ta phát hiện nguy hiểm tốt hơn, với ít cảnh báo giả hơn.

`hong({ eyes:"surprise" });`

h: Và *điều đó* sẽ giúp bảo vệ chúng ta khỏi tổn thương!

`hong({ eyes:"normal", mouth:"normal" });`

h: Do đó: đây *là* khóa đào tạo tự vệ.

`bb({ eyes:"normal_r" })`

b: Hừm. Mình đã mong chờ nhiều hơn thế này:

```
Game.FORCE_CANT_SKIP = true;
Game.clearText();
hong({ eyes:"sad", mouth:"smile" });
bb({ body:"karate_1" });
sfx("hiya");
```

(...1001)

`Game.FORCE_CANT_SKIP = false;`

(#act4_something_else)

# act4_harm_skills_work

`bb({ eyes:"normal" });`

h: Đúng vậy, không có cách nào để bảo vệ hoàn toàn bản thân mình...

`hong({ body:"one_up" });`

h: Nhưng ngay cả khi chỉ cải thiện được 1% cũng vẫn có giá trị, đúng không?

```
bb({ eyes:"annoyed" });
hong({ normal:"one_up" });
```

b: Cậu đang nhìn cái ly không phải 99% trống, mà là 1% đầy à?

`bb({ eyes:"normal" });`

h: 1% đó vẫn có giá trị nếu cậu bị mắc kẹt trong sa mạc.

`bb({ eyes:"closed" });`

b: Vậy thì, cạn ly thôi.

(#act4_something_else)

# act4_harm_skills_overboard

`bb({ body:"chest", eyes:"annoyed" })`

b: Ý cậu là lý do cậu phớt lờ những lời cảnh báo của mình là vì *mình* đã quá cẩn thận sao!

`bb({ body:"normal", eyes:"normal" })`

h: Không, cậu đúng. Mình nên làm mọi thứ một cách vừa phải. Tất cả đều phải có chừng mực.

`bb({ eyes:"suspect" })`

b: Xin lỗi, *TẤT CẢ* đều phải có chừng mực sao?

`hong({ eyes:"annoyed" })`

h: *Một số thứ vừa đủ* trong chừng mực.

```
bb({ eyes:"closed" });
hong({ eyes:"normal" });
```

b: Cảm ơn cậu đã làm cho những điều cậu nói trở nên nhất quán với nhau.

(#act4_something_else)


# act4_harm_exposure

`bb({ mouth:"scream_talk", eyes:"scream", MOUTH_LOCK:true });`

b: *GÌ CƠ*

```
bb({ mouth:"narrow", eyes:"suspect" });
hong({ body:"one_up" });
```

h: Ý tớ là, giả sử một con chó sợ sấm sét.

`hong({ body:"hands_1" });`

h: Một mẹo mà những người huấn luyện sử dụng là phát một đoạn ghi âm tiếng sấm ở âm lượng thấp, rồi cho chó một miếng thưởng khi nó giữ được bình tĩnh.

`hong({ body:"hands_2" });`

h: Sau vài ngày, người huấn luyện tăng dần âm lượng cho đến khi chú chó đã vượt qua nỗi sợ tiếng sấm.

```
hong({ body:"normal", eyes:"surprise" });
bb({ mouth:"normal", eyes:"normal" });
```

h: Nó được gọi là liệu pháp tiếp xúc!

`hong({ body:"point", eyes:"normal" });`

h: Vì cậu là chó, nên nó cũng sẽ có tác dụng với cậu đúng không? Tất cả các loài động vật có vú đều có phản ứng chiến đấu hoặc bỏ chạy giống nhau.

`hong({ body:"normal" });`

[Nếu chúng ta làm quen quá nhiều thì sao?](#act4_harm_exposure_overboard)

[Sẽ thế nào nếu chúng ta gặp phải nguy hiểm *thực sự*?](#act4_harm_exposure_hurt)

[Tớ là sói, không phải chó.](#act4_harm_exposure_dog) `bb({ eyes:"suspect" })`

# act4_harm_exposure_dog

h: Và mình sẽ thể hiện sự tử tế và kiên nhẫn cho đến khi cậu trở thành một chú chó con dễ thương.

`bb({ MOUTH_LOCK:true })`

b: ...

`bb({ eyes:"sad", mouth:"smile" })`

b: hòa nhé.

(#act4_something_else)

# act4_harm_exposure_overboard

`bb({ eyes:"annoyed" })`

b: Chúng ta *vừa* thấy điều gì xảy ra nếu cậu chặn đứng nỗi sợ – cậu đã đặt mình vào những tình huống *thực sự* nguy hiểm.

`bb({ eyes:"angry_r", body:"one_up" })`

b: Hơn nữa, liệu việc kháng cự *quá* mức có biến chúng ta thành những kẻ tâm thần không?

`bb({ mouth:"scream", eyes:"scream", body:"two_up" })`

b: Chúng ta sẽ sớm được thưởng thức những món ăn ngon khi xem phim ^khiêu dâm giết người!^

`hong({ eyes:"annoyed" })`

h: Tớ... nghĩ có một ranh giới giữa điều đó và tiếng sấm.

`bb({ body:"normal", mouth:"normal", eyes:"suspect" })`

b: Nhưng chính xác là *đâu*, cậu ơi? *Đâu?!*

`hong({ eyes:"surprise", body:"one_up" })`

h: Mình không biết. Nhưng *cậu* có thể giúp mình!

`hong({ eyes:"normal", body:"normal" })`

h: Làm việc và thương lượng với cậu, chúng ta sẽ vạch ra được ranh giới đó.

`bb({ body:"paw", mouth:"narrow", eyes:"closed" })`

b: Được rồi. Nhưng tớ không có ngón tay cái, nên cậu phải là người vẽ ra ranh giới đó.

(#act4_something_else)

# act4_harm_exposure_hurt

`bb({ body:"two_up", eyes:"angry_r" })`

{{if _.INJURED}}
b: Chẳng hạn như: chúng ta vừa nhảy từ một cái *mái nhà!*
{{/if}}

{{if !_.INJURED}}
b: Chẳng hạn như: chúng ta suýt nhảy từ một cái *mái nhà!*
{{/if}}

```
hong({ eyes:"annoyed" });
bb({ body:"normal", eyes:"annoyed" });
```

h: Không, cậu nói đúng. Một người *có thể* đi quá xa.

`hong({ eyes:"normal" });`

h: Nhưng đó là lý do, nếu chúng ta làm liệu pháp tiếp xúc, chúng ta sẽ bắt đầu từ những bước nhỏ và dần dần tăng lên.

h: Ngay trước khi chúng ta đối mặt với *nguy hiểm thực sự*, chúng ta sẽ dừng lại.

`bb({ eyes:"annoyed_r", mouth:"narrow" });`

b: Ừ, mình sẽ vạch ra ranh giới giữa việc nghe tiếng sấm lớn và đứng giữa cơn bão với một chiếc mũ nhọn cao.

(#act4_something_else)

# act4_thanks

`_.num_thanks += 1`

{{if _.num_thanks==1}}
(#act4_thanks_1)
{{/if}}

{{if _.num_thanks==2}}
(#act4_thanks_2)
{{/if}}

{{if _.num_thanks==3}}
(#act4_thanks_3)
{{/if}}

# act4_thanks_1

`bb({ MOUTH_LOCK:true })`

b: ...

`bb({ eyes:"annoyed" })`

b: Khoan đã, không có tranh cãi nào về cảm giác của mình sao? Chỉ có... "cảm ơn" thôi à?

`hong({ eyes:"surprise", body:"shrug" })`

h: Ừ! Cảm ơn vì đã thể hiện sự lo lắng cho tớ. {{_.thanks_for}}.

```
bb({ eyes:"closed_annoyed", MOUTH_LOCK:true });
hong({ eyes:"normal", body:"normal" });
```

b: ...

h: Cậu ổn không?

`bb({ eyes:"super_sad", mouth:"narrow" });`

b: Cậu chưa bao giờ nói "cảm ơn" tớ trước đây.

`hong({ mouth:"smile" });`

h: Ôi, cậu sói mập mạp và hay hoảng sợ.

(#act4_something_else)

# act4_thanks_2

h: Dù cậu có phản ứng thái quá, tớ vẫn cảm kích cậu vì đã chăm sóc cho tớ {{_.thanks_for}}.

`bb({ eyes:"annoyed" })`

b: Chờ đã... cậu không chỉ lặp lại "cảm ơn" để tránh nói chuyện về những nỗi sợ này, phải không?

```
bb({ eyes:"normal" });
hong({ eyes:"annoyed", body:"chin" });
```

h: Chà, mọi thứ phức tạp, và tớ không phải lúc nào cũng có sẵn câu trả lời.

`hong({ eyes:"annoyed_l", body:"one_up" })`

h: Cuộc sống đâu có đưa cho cậu sẵn một danh sách 3 câu trả lời để chọn.

`hong({ eyes:"normal", mouth:"smile", body:"normal" })`

h: Nhưng giờ đây, tớ ít nhất có thể nói cảm ơn.  

b: Cảm ơn cậu nữa, vì đã lắng nghe tớ một cách kiên nhẫn.

`bb({ eyes:"closed" });`

b: Cậu, cái sinh vật không lông nhỏ bé.

(#act4_something_else)

# act4_thanks_3

h: Dù việc cậu sủa khiến tớ sợ, nhưng cậu chỉ đang cố gắng bảo vệ tớ thôi mà {{_.thanks_for}}.

`bb({ eyes:"smile_r" });`

b: Được rồi, nếu cậu cứ khen tớ như vậy, thì internet sẽ có những ý tưởng kỳ quái về chúng ta đấy.

```
bb({ eyes:"smile" });
hong({ eyes:"annoyed" });
```

h: Thôi nào, tớ chỉ là một đứa trẻ đại học dễ tổn thương và cậu là một con sói to lớn, đáng sợ. Có thể điều tồi tệ nhất sẽ là gì--

`hong({ eyes:"normal", body:"point" });`

h: Thực ra, đừng có trả lời cái đó.

(#act4_something_else)




# act4_alone

```
_.a4_talked_about_alone = true;
_.a4_fears_discussed += 1;
```

`bb({ eyes:"sad_d" });`

b: Tớ muốn chắc chắn rằng cậu sẽ thỏa mãn được nhu cầu sâu sắc của con người về việc thuộc về...

`bb({ eyes:"sad_u" });`

b: Nhưng tớ lo rằng nếu ai đó biết về chúng ta – về bản chất *thật* của chúng ta – thì họ sẽ bị dọa và chạy mất.

`bb({ eyes:"sad" });`

{{if _.a4_fears_discussed==1}}
b: Tớ không biết, đủ rồi với việc *tớ* chọn câu tiếp theo. Cậu nói gì, con người?
{{/if}}

{{if _.a4_fears_discussed==2}}
b: Lại là cậu, con người. Cậu nghĩ sao?
{{/if}}

{{if _.a4_fears_discussed==3}}
b: Còn ý kiến nào khác không, con người ?
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Tớ đồng ý: hãy cải thiện đời sống xã hội.](#act4_alone_skills)

[Tớ nghĩ mọi người thích chúng ta. Cùng tìm hiểu nhé?](#act4_alone_experiment)

[Cảm ơn cậu.](#act4_thanks) `_.thanks_for = "social belonging";`

# act4_alone_skills

```
bb({ eyes:"normal" });
hong({ body:"chin" });
```

h: Chúng ta có thể luyện tập những kỹ năng như đặt câu hỏi, lắng nghe và đồng cảm, cũng như trở nên cởi mở và dễ tổn thương, v.v.?

`hong({ eyes:"normal_l" });`

h: Hoặc tạo thói quen xã hội tốt hơn, như lên lịch thời gian gặp gỡ bạn bè hoặc thường xuyên tham gia các buổi gặp gỡ?

`hong({ body:"one_up" });`

h: Cũng có thể học cách thoải mái hơn với sự từ chối.

`hong({ eyes:"normal" });`

h: Hoặc học cách nhận ra khi mọi người *không* từ chối bọn mình, mà họ chỉ mệt mỏi hoặc có gương mặt khó ưa tự nhiên.

```
hong({ body:"normal" });
bb({ eyes:"annoyed_r" });
```

b: Liệu học cách giao tiếp xã hội có thực sự làm được không? Cậu có nghĩ mình sẽ tiến bộ nếu luyện tập không?

[Như thế không phải là *thao túng* sao?](#act4_alone_skills_manipulative)

[Vậy không phải sẽ *dễ bị thao túng hơn sao?*](#act4_alone_skills_manipulated)

[Nếu chúng ta vẫn thất bại thì sao?](#act4_alone_skills_fail)

# act4_alone_skills_manipulative

`bb({ eyes:"suspect" });`

b: Những kẻ giết người hàng loạt có thể đọc được cảm xúc của nạn nhân không phải là rất giỏi về "sự đồng cảm" sao?

`bb({ eyes:"annoyed" });`

b: Charles Manson không phải đã kết bạn và có ảnh hưởng đến mọi người sao?

`hong({ eyes:"annoyed", body:"chin" });`

h: Không, cậu nói đúng.

h: "Kỹ năng xã hội" chẳng có nghĩa lý gì nếu chúng ta không thật sự quan tâm *đến* mọi người.

`hong({ body:"normal" });`

h: Nói chung, chỉ cần đừng có làm người ^khốn nạn^.

`bb({ eyes:"annoyed", mouth:"smile" });`

b: Đó chính là một câu chú thích cho tấm poster động lực đấy.

`hong({ body:"shrug", mouth:"narrow" });`

h: “Đừng Làm Một ^Con khốn ^™”

(#act4_something_else)

# act4_alone_skills_manipulated

`bb({ eyes:"angry" })`

b: Chúng ta sẽ trở thành một tấm thảm chào đón, vừa nói "Xin vui lòng" và "Cảm ơn" khi mọi người chùi chân lên chúng ta!

`bb({ mouth:"scream", eyes:"scream" })`

b: Chúng ta sẽ ^hôn mông^ nhiều đến nỗi trông như đang tô son màu nâu vậy!

```
bb({ mouth:"normal", eyes:"normal" });
hong( body:"chin" });
```

h: Không, cậu nói đúng. "Kỹ năng xã hội" không thể chỉ là làm hài lòng người khác, mà còn phải về việc thiết lập *ranh giới.*

`hong( body:"one_up" });`

h: Chúng ta không thể mời người khác vào nhà mình, nếu như không có bức tường nào để giữ cho ngôi nhà ấy.

```
hong( eyes:"angry", mouth:"narrow" });
bb( eyes:"annoyed", mouth:"smile" });
```

h: Còn nữa... về hình ảnh son môi đó... *ư??*

(#act4_something_else)

# act4_alone_skills_fail

`bb({ eyes:"annoyed" });`

h: Chúng ta có thể thất bại. Thật ra, chúng ta *sẽ* thất bại.

```
bb({ eyes:"normal" });
hong({ eyes:"surprise", body:"shrug" });
```

h: Và điều đó không sao cả! Thất bại là cách mà bất kỳ ai cũng học hỏi điều gì đó mới mẻ ngay từ đầu!

`hong({ body:"normal", eyes:"normal" });`

h: Vậy thì hãy cùng nhau thất bại và tiến về phía trước, được chứ?

`bb({ eyes:"normal_r" });`

b: Chắc rồi, tớ nghĩ vậy... trong tình huống xấu nhất, chúng ta có thể chỉ cần bỏ trốn và đổi sang một danh tính mới.

`bb({ eyes:"normal" });`

h: Ừ, tớ nghĩ giờ chỉ tốn hai bitcoin thôi.

(#act4_something_else)

# act4_alone_experiment

```
hong({ body:"one_up" });
bb({ eyes:"normal" });
```

h: Chúng ta có thể thử một số thí nghiệm!

`hong({ body:"chin" });`

h: Chúng ta có thể gọi một người bạn để đi chơi, nối lại liên lạc với một người bạn cũ, hoặc thậm chí chỉ trò chuyện với một nhân viên pha chế.

`hong({ body:"normal" });`

h: Tớ nghĩ chúng ta có thể sẽ thấy mình dễ thương hơn những gì mình tưởng.

`bb({ eyes:"annoyed" });`

[Nếu đây là những "chiến thắng" nhỏ nhặt không đáng thì sao?](#act4_alone_experiment_cheap)

[Nếu điều này trở thành áp lực cho người khác thì sao?](#act4_alone_experiment_burden)

[Nhưng nói chuyện phiếm không phải là con người *thực* của chúng ta!](#act4_alone_experiment_real_us)

# act4_alone_experiment_real_us

`bb({ eyes:"sad" });`

b: Nếu chúng ta chỉ nở một nụ cười hời hợt, thì sẽ không bao giờ thật sự kết nối được với ai cả,

`bb({ eyes:"super_sad" });`

b: *Nhưng* nếu chúng ta mở lòng ra, người khác sẽ thấy hết những gì rối ren bên trong chúng ta!

`hong({body:"chin", mouth:"narrow", MOUTH_LOCK:true})`

h: ...

```
hong({body:"normal", mouth:"normal"});
bb({eyes:"normal"});
```

h: Lăn qua.

b: Gì cơ.

`hong({body:"hands_1"})`

h: Khi chó muốn thể hiện tình yêu và sự tin tưởng, chúng sẽ làm cho mình trở nên dễ tổn thương bằng cách để lộ bụng ra.

`hong({body:"one_up"})`

h: Có thể bây giờ chúng ta chưa *đủ* an toàn để trở nên quá dễ tổn thương, nhưng với đủ sự rèn luyện,

`hong({body:"normal", eyes:"surprise"})`

h: Một ngày nào đó, chúng ta có thể cho mọi người thấy bản thân thật sự của mình – hết rối ren, hết nhân tính.

```
hong({eyes:"normal"});
bb({ eyes:"super_sad", mouth:"smile", body:"chest" });
```

b: Tớ sẽ lăn qua nếu cậu cho tớ một món quà.

`bb({ eyes:"normal", mouth:"normal" });`

h: Không.

(#act4_something_else)


# act4_alone_experiment_cheap

b: Nói "xin chào" với nhân viên pha chế không hẳn là thành tích huy chương vàng trong Social Butterfly Olympics đâu.

```
hong({ body:"point", eyes:"surprise" });
bb({ eyes:"normal" });
```

h: Đối với *chúng ta* thì đúng vậy!

`hong({ body:"one_up", eyes:"annoyed" });`

h: Trong lĩnh vực xã hội, chúng ta còn không ở hạng nhẹ, mà giống như... hạng quark vậy.

`hong({ body:"normal", eyes:"normal" });`

h: Nếu chúng ta phải bắt đầu với những chiến thắng nhỏ và rẻ tiền, thì cứ vậy đi. Phải bước lên bậc thang thứ nhất trước khi lên đến bậc thang thứ 1000.

b: Đúng vậy! Có thể sau khi nói "Xin chào", chúng ta có thể tiến đến việc nói...

`bb({ body:"two_up", mouth:"smile", eyes:"smile_u" });`

b: *"Cậu khỏe không?"*

`hong({ body:"shrug", mouth:"smile", eyes:"surprise_l" });`

h: *"Không có gì nhiều!"*

(#act4_something_else)

# act4_alone_experiment_burden

`bb({ eyes:"suspect_r" })`

b: Có khi nhân viên pha chế chỉ muốn pha cà phê thôi, chứ không phải trở thành *vật thí nghiệm* để xem kỹ năng xã hội của chúng ta có tệ không.

`bb({ eyes:"annoyed" })`

h: Ừ thì, nếu hóa ra chúng ta *đang* trở thành gánh nặng thật...

```
hong({ eyes:"surprise" });
bb({ eyes:"normal" });
```

h: Thì biết được điều đó cũng tốt mà!

`hong({ eyes:"normal" });`

h: Sau đó, chúng ta có thể học cách chủ động hỏi mọi người về những gì họ cảm thấy thoải mái, để hiểu và tôn trọng ranh giới của họ.

```
hong({ eyes:"annoyed_l", mouth:"narrow" });
bb({ eyes:"annoyed", mouth:"smile" });
```

h: Cậu biết đấy, mấy cái "kỹ năng giao tiếp cá nhân" ^vớ vẩn^ mà ta thấy trong tờ rơi của các cố vấn ấy.

(#act4_something_else)



# act4_bad

```
_.a4_talked_about_bad = true;
_.a4_fears_discussed += 1;
```

`bb({ eyes:"annoyed_r" })`

b: Tớ muốn bảo vệ những nhu cầu đạo đức của cậu, cái động lực để trở thành một người tốt hơn,

`bb({ eyes:"sad_d" })`

b: Nhưng tớ cứ cảm thấy sâu thẳm bên trong, tớ thực sự... tan vỡ.

`bb({ body:"two_up", eyes:"angry" })`

{{if _.INJURED}}
b: Và đừng nói với tớ là chúng ta *không* rối loạn. Chúng ta đã nhảy từ *mái nhà* xuống.
{{/if}}

{{if !_.INJURED}}
b: Và đừng nói với tớ là chúng ta *không* rối loạn. Chúng ta đã suýt nhảy từ *mái nhà* xuống.
{{/if}}

`bb({ body:"normal", eyes:"sad" })`

{{if _.a4_fears_discussed==1}}
b: Tớ không biết, đủ rồi với việc *tớ* chọn những gì sẽ nói tiếp theo. Cậu *nói* gì, con người?
{{/if}}

{{if _.a4_fears_discussed==2}}
b: Một lần nữa, trở lại với cậu, con người. Cậu nghĩ sao?
{{/if}}

{{if _.a4_fears_discussed==3}}
b: Còn suy nghĩ gì nữa không, con người?
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Vậy cậu tổn thương? Hãy đi chữa lành bản thân thôi..](#act4_bad_fix)

[Vậy cậu tổn thương? Hãy chấp nhận điều đó.](#act4_bad_accept)

[Cảm ơn cậu.](#act4_thanks) `_.thanks_for = "moral well-being";`

# act4_bad_fix

```
bb({eyes:"normal"});
hong({body:"chin"});
```

h: Chúng ta có thể từ từ xây dựng những thói quen tốt hơn, làm cho cuộc sống của mình phù hợp hơn với những gì chúng ta trân trọng,

`hong({body:"one_up"});`

h: Và nếu cần, chúng ta có thể tìm sự giúp đỡ từ chuyên gia – một nhà trị liệu hoặc cố vấn.

`hong({body:"normal"});`

h: Có những cách để chữa lành cho bản thân.

[Hãy làm gì nếu chúng ta không thể sửa mọi thứ?](#act4_bad_fix_cant)

[Hãy làm gì nếu chúng ta phải sửa *quá nhiều*?](#act4_bad_fix_too_much)

[Chúng ta không đủ tiền để trả cho trị liệu tâm lý.](#act4_bad_fix_afford)

# act4_bad_fix_cant

`hong({eyes:"annoyed"});`

h: Không, tớ nghĩ cậu nói đúng.

h: Chúng ta không thể sửa tất cả mọi thứ.

`bb({mouth:"scream", eyes:"scream_sad"});`

b: Ahhh, tớ biết mà, chúng ta luôn dễ tổn thương!

`hong({eyes:"surprise"});`

h: Nhưng ít nhất chúng ta có thể *ít* tổn thương hơn.

```
bb({mouth:"normal", eyes:"annoyed"});
hong({eyes:"sad", mouth:"smile"});
```

h: Vết sẹo sẽ lành theo thời gian, nhưng chúng sẽ không bao giờ biến mất. Và điều đó cũng không sao cả.

`bb({eyes:"annoyed_r"});`

b: Tớ nghĩ vậy. Hơn nữa,

```
Game.FORCE_TEXT_Y = 460;
Game.clearText();
publish("act4-sexy", [true]);
```

b: Vết sẹo thật *gợi cảm.*

```
Game.FORCE_TEXT_Y = -1;
Game.clearText();
publish("act4-sexy", [false]);
bb({body:"chest", mouth:"smile_talk", MOUTH_LOCK:true, eyes:"sexy"}, 0);
hong({eyes:"normal", mouth:"normal"}, 0);
```

h: Làm ơn đừng làm vậy.

(#act4_something_else)

# act4_bad_fix_too_much

`bb({ eyes:"angry_d" })`

b: Thật là khó chịu khi phải thừa nhận, nhưng... một phần trong tớ *muốn* có chứng rối loạn này.

`bb({ eyes:"angry" })`

b: Ý tớ là, nếu không có nó, chúng ta chẳng phải sẽ *buồn chán* sao?

`bb({ eyes:"sad_r", body:"one_up" })`

b: Nếu mọi thứ không có chút lộn xộn nào, liệu nghệ thuật của chúng ta có bị nhạt nhòa và kém thú vị không?

`bb({ eyes:"sad_u", body:"two_up" })`

b: Nếu không có chứng rối loạn, chẳng phải chúng ta sẽ không thể kết nối với những người bạn có chứng rối loạn đó sao?

`bb({ eyes:"sad", body:"chest" })`

b: Nếu một ngày nào đó chúng ta hài lòng với cuộc sống, chẳng phải chúng ta sẽ ngừng thúc đẩy bản thân làm những điều tuyệt vời sao?

`hong({ MOUTH_LOCK:true })`

h: ...

h: Nếu chúng ta thậm chí còn sợ... "hết nỗi sợ"...

h: Tớ không nghĩ là chúng ta sẽ hết nỗi sợ đâu.

`bb({ eyes:"smile_u", body:"normal", mouth:"smile" })`

b: Ồ, đúng rồi! Uầy! Thật nhẹ nhõm!

(#act4_something_else)

# act4_bad_fix_afford

`bb({ body:"one_up", eyes:"sexy", mouth:"normal" })`

b: "Bác sĩ, tôi lo lắng vì phải trả 100 đô la/giờ chỉ để nghe ông hỏi *cảm giác của bạn như thế nào?*"

`bb({ body:"paw", eyes:"closed", mouth:"narrow" })`

b: "Mm-hmm. Và điều đó khiến cậu cảm thấy thế nào?"

```
bb({ body:"normal", eyes:"normal", mouth:"normal" });
hong({ eyes:"sad" });
```

h: Không, đó là một lo lắng hoàn toàn hợp lý.

`hong({ eyes:"annoyed", mouth:"sad" });`

h: Và thật sự thì thật tệ khi chăm sóc sức khỏe tâm thần không phải là điều mà nhiều người có thể chi trả.

`hong({ eyes:"normal", mouth:"normal" });`

h: Vẫn có một số lựa chọn rẻ hoặc miễn phí:

`hong({ body:"chin" })`

h: Các nhóm hỗ trợ, liệu pháp trực tuyến, trung tâm y tế sinh viên hoặc tổ chức phi lợi nhuận...

`hong({ body:"hands_1" })`

h: Xây dựng thói quen như thiền, ngủ đủ giấc, trò chuyện thường xuyên với bạn bè, học hỏi những điều mới...

`hong({ body:"hands_2" })`

h: Đi đến thư viện để mượn sách bài tập cho các liệu pháp tâm lý dựa có cơ sở khoa học...

`hong({ body:"one_up" })`

h: Có một danh sách đầy đủ các tài nguyên ở cuối trò chơi này!

```
hong({ body:"normal" });
bb({ eyes:"annoyed", mouth:"narrow" });
```

b: Chà, *bức tường thứ tư* đó đã không tồn tại lâu.

`hong({ body:"point" });`

h: Có những thứ quan trọng hơn quy ước về cốt truyện. Chẳng hạn như sức khỏe tâm thần.

(#act4_something_else)


# act4_bad_accept

```
bb({ eyes:"normal" });
hong({ eyes:"normal_l", body:"one_up", mouth:"narrow" });
```

h: Ý mình là, đó là điều mà các nhà trị liệu nói đúng không? Chấp nhận tất cả cảm xúc của cậu, ngay cả những cảm xúc tiêu cực?

```
bb({ eyes:"annoyed" });
hong({ eyes:"normal", body:"normal", mouth:"normal" });
```

b: Wait.

["Chấp nhận" có nghĩa là *bỏ cuộc*?](#act4_bad_accept_give_up)

[Có nghĩa là 'đồng ý' khi nói 'chấp nhận' phải không?](#act4_bad_accept_approve)

["Chấp nhận" theo nghĩa đen phải không?](#act4_bad_accept_literally)

# act4_bad_accept_give_up

`bb({ eyes:"angry", body:"one_up" });`

b: Cậu nghĩ Martin Luther King sẽ nói, "Ôi, chúng ta không thể ngồi ở hàng ghế phía trước của xe buýt, hãy cứ *chấp nhận* đi?"

`bb({ eyes:"angry_r", body:"two_up" });`

b: Tại sao ngành công nghiệp tự lực (Self-Help) lại nghĩ rằng đầu hàng hay từ bỏ là lựa chọn khôn ngoan?

`bb({ eyes:"annoyed", body:"normal" });`

h: Mình nghĩ các nhà trị liệu có nghĩ là "chấp nhận" những điều xấu như là: thừa nhận chúng tồn tại và khó thay đổi.

h: Nhưng không nhất thiết là từ bỏ cam kết thay đổi.

`bb({ eyes:"suspect" });`

b: Thì các nhà trị liệu nên nói là *thừa nhận*, chứ không phải *chấp nhận*.

`hong({ body:"chin", eyes:"annoyed" });`

h: Ừ, nghĩ lại thì "chấp nhận" hơi khó hiểu thật.

`bb({ eyes:"closed", mouth:"narrow" });`

b: Thôi, tớ *thừa nhận* điều đó.

(#act4_something_else)

# act4_bad_accept_approve

`bb({ eyes:"angry" });`

b: Như thể việc chúng ta bị hỏng là *tốt* hay sao? Không!

`bb({ eyes:"angry_r", body:"one_up" });`

b: Tất cả những nhà biên kịch Hollywood đã lãng mạn hóa bệnh tâm thần đều đầy rác rưởi!

`bb({ eyes:"angry", body:"two_up" });`

b: Có rối loạn tâm thần thật sự *tệ!* Nó cướp đi *cuộc sống* của mọi người! Tại sao chúng ta lại phải "chấp nhận" điều đó chứ?!

`bb({ body:"normal" });`

h: Mình nghĩ các nhà trị liệu muốn nói "chấp nhận" cảm xúc của mình có nghĩa là: kiên nhẫn với chúng.

```
hong({ body:"one_up" });
bb({ eyes:"normal" });
```

h: Giống như việc vật lộn trong cát lún làm cậu chìm nhanh hơn, và giải pháp là kiên nhẫn nằm thẳng ra.

`hong({ eyes:"surprise" });`

{{if _.INJURED}}
h: Đấu tranh chống lại cậu, nỗi sợ của tớ, đã khiến tớ nhảy xuống một cái mái nhà.
{{/if}}

{{if !_.INJURED}}
h: Đấu tranh chống lại cậu, nỗi sợ của tớ, suýt nữa đã khiến tớ nhảy xuống một cái mái nhà.
{{/if}}

`hong({ body:"normal", eyes:"normal" });`

h: Thay vào đó, giải pháp là làm những gì chúng ta đang làm bây giờ – không phải để chiến đấu, mà là kiên nhẫn ở bên nhau.

`bb({ eyes:"annoyed" });`

b: Vậy thì họ nên nói *điều đó* thay vì dùng một từ gây tranh cãi như "chấp nhận".

`hong({ body:"chin", eyes:"annoyed" });`

h: Thật ra, nghĩ lại thì từ "chấp nhận" cũng không hay cho lắm.

`bb({ eyes:"closed_annoyed", mouth:"narrow" });`

b: Tớ không chấp nhận từ "chấp nhận".

(#act4_something_else)

# act4_bad_accept_literally

`bb({ eyes:"sad", body:"one_up" });`

b: Nhưng tớ đã biết rằng cậu không nên hiểu tớ theo nghĩa đen!

`bb({ eyes:"sad_u", body:"two_up" });`

b: Vấn đề chính là tớ muốn giúp cậu, nhưng tớ lại kém trong việc sử dụng từ ngữ để làm điều đó!

`bb({ eyes:"sad", body:"normal" });`

h: Tớ nghĩ các nhà trị liệu muốn nói "chấp nhận" cảm xúc của cậu có nghĩa là: "đừng chiến đấu hay phớt lờ chúng."

`hong({ eyes:"surprise", body:"one_up" });`

h: Để lắng nghe cậu, làm việc *cùng* cậu, nhưng không lấy những gì cậu nói là chân lý 100%.

```
hong({ eyes:"normal", body:"normal" });
bb({ eyes:"annoyed", mouth:"normal" });`
```

b: Vậy thì các nhà trị liệu nên nói *điều đó* thay vì dùng những từ mơ hồ gây nhầm lẫn như "chấp nhận".

`hong({ body:"chin", eyes:"annoyed" });`

h: Chắc họ cũng không giỏi lắm trong việc sử dụng từ ngữ.

(#act4_something_else)




# act4_something_else

```
bb({ body:"normal", mouth:"normal", eyes:"normal" });
hong({ body:"normal", mouth:"normal", eyes:"normal" });
```

{{if _.a4_fears_discussed==1}}
h: Dù sao, cậu còn muốn trò chuyện về điều gì khác không?
{{/if}}

{{if _.a4_fears_discussed==2}}
h: Vậy, còn điều gì khác trong trái tim nặng trĩu của cậu không?
{{/if}}

{{if _.a4_fears_discussed==3}}
(#act4_something_else_2)
{{/if}}

{{if _.a4_talked_about_harm!=true}}
[Mình sợ bị tổn thương.](#act4_harm)
{{/if}}

{{if _.a4_talked_about_alone!=true}}
[Tớ sợ không được yêu thương.](#act4_alone)
{{/if}}

{{if _.a4_talked_about_bad!=true}}
[Mình sợ trở thành người xấu](#act4_bad)
{{/if}}

[Không, bây giờ thì ổn rồi.](#act4c_prelude)

# act4_something_else_2

h: Được rồi, tớ nghĩ chúng ta đã nói về tất cả nỗi sợ rồi.

b: Ừ, chỉ có ba nỗi sợ thôi.

h: Đúng rồi, chính xác là ba.

b: Thật tiện lợi.

(#act4c)

# act4c_prelude

h: Nói chuyện vui ghê, cả đội.

(#act4c)

# act4c

```
Game.clearText();
music(null,{fade:3});
bb({body:"normal", eyes:"normal", mouth:"normal", MOUTH_LOCK:true},0);
hong({body:"normal", eyes:"normal", mouth:"normal"},0);
```

b: ...

`hong({MOUTH_LOCK:true},0)`

h: ...

`bb({eyes:"annoyed_d"})`

b: Không phải chỉ là *trò chơi*, cậu biết chứ.

`bb({eyes:"angry_d", body:"one_up"})`

b: Xây dựng một mối quan hệ lành mạnh với cảm xúc của cậu không đơn giản như việc bấm nút trên màn hình.

`bb({eyes:"sad", body:"normal"})`

b: *Liệu* chúng ta có thể thực sự hòa hợp không? 

b: *Liệu* chúng ta có thể làm việc cùng nhau, như một đội?

`hong({eyes:"sad", body:"one_up"})`

h: Well,

```
hong({eyes:"surprise_l"});
bb({eyes:"normal"});
```

a: C-cậu gì ơi...

```
Game.clearText();
publish("act4-in-2");
music('campus', {volume:0.5, fade:1});
```

(...2101)

(#act4d)

# act4d

`Game.WORDS_HEIGHT_BOTTOM = 221;`

`publish("act4", ["alshire", 0]);`

a: C-cậu có phiền nếu tớ ngồi cùng cậu trong bữa trưa không?

`publish("act4", ["alshire", 1]);`

{{if _.TOP_FEAR=="harm"}}
s: *Đây* là người mà cậu thích à? Tại sao họ lại ngồi một mình như một kẻ sát nhân tâm thần vậy?
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: Hỏi người mà cậu thích xem có thể ngồi cùng không? Cậu có biết mình *thèm khát* có người ăn cùng như thế nào không?!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: *Người mà cậu thích* là người như thế này sao? Cậu đang phá vỡ sự bình yên của họ! Chúng ta thật sự phiền phức!
{{/if}}

`publish("act4", ["alshire", 2]);`

a: T- tớ ý là... nếu không thì cũng không sao, tớ chỉ...

`publish("act4", ["alshire", 3]);`

`Game.OVERRIDE_CHOICE_SPEAKER = "h2"`

[Đợi đã, hình như mình đã thấy bạn ở bữa tiệc thì phải?](#act4d_recognition) `publish("act4", ["hong_to_alshire",1])`

[Vâng, tất nhiên rồi! Đến đây nào.](#act4d_yes) `publish("act4", ["hong_to_alshire",2])`

[Xin lỗi, giờ mình cần thời gian riêng tư.](#act4d_no) `publish("act4", ["hong_to_alshire",8])`

# act4d_recognition

`publish("act4", ["hong_to_alshire",2]);`

h2: Ừ, cậu đã ở trên ghế sofa! Tại bữa tiệc đầu tiên mà tớ tham gia...

`publish("act4", ["hong_to_alshire",10]);`

{{if _.a2_ending=="fight"}}
h2: Nơi tớ bị cơn hoảng loạn và đấm vào mặt chủ bữa tiệc.
{{/if}}

{{if _.a2_ending=="flight"}}
h2: Nơi tớ bị hoảng sợ và chạy ra ngoài khóc.
{{/if}}

```
publish("act4", ["hong_to_alshire", 0]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: Khoan đã, cậu ơi, có thể chúng ta đang làm họ không thoải mái.

```
publish("act4", ["hong_to_alshire", 3]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: Ồ, tớ không có ý làm cậu bối rối đâu!

`publish("act4", ["hong_to_alshire",4]);`

h2: Chỉ là nhớ đến một gương mặt thân thiện thôi mà.

```
publish("act4", ["hong_to_alshire",5]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: AHHHHH, MÌNH ĐÃ BIẾT MÀ! HỌ LÀ MỘT KẺ TÂM THẦN BỊ ĐIỀU KHIỂN BỞI CẢM XÚC!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: AAHHH, ẤN TƯỢNG ĐẦU TIÊN MÀ CHÚNG TA ĐỂ LẠI LÀ "CHỨNG KIẾN NỖI ĐAU CỦA CẬU"! CÓ NGHĨA LÀ HỌ GHÉT CHÚNG TA!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: AAAHHH, CHÚNG TA KHIẾN AI ĐÓ NHỚ ĐẾN MỘT SỰ KIỆN TỔN THƯƠNG. SỰ HIỆN DIỆN CỦA CHÚNG TA LÀM ĐAU KHỔ NGƯỜI KHÁC!
{{/if}}

(#act4e)

# act4d_yes

```
publish("act4", ["hong_to_alshire", 5]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: Đợi đã, cậu ơi, họ có vẻ không thoải mái.

```
publish("act4", ["hong_to_alshire", 6]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: À, không có áp lực gì đâu!

`publish("act4", ["hong_to_alshire", 4]);`

h2: Mình chỉ nói rằng, bạn có thể ngồi đây nếu muốn.

```
publish("act4", ["hong_to_alshire", 5]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: HỌ QUÁ THÂN THIỆN! NHƯ TED BUNDY, KẺ GIẾT NGƯỜI!{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: HỌ CHỈ ĐANG CƯ XỬ NHẰM THỂ HIỆN SỰ TỐT BỤNG! KHÔNG AI THỰC SỰ MUỐN GẦN GŨI CHÚNG TA!{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: AHHH CẬU LUÔN KHIẾN NGƯỜI KHÁC CẢM THẤY KHÓ XỬ! CẬU LÀ MỘT VẾT NHƠ TRÊN ĐỜI NÀY!
{{/if}}

(#act4e)

# act4d_no

```
publish("act4", ["hong_to_alshire", 9]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: Chờ đã, cậu ơi, có thể chúng ta đang khiến họ cảm thấy không thoải mái.

```
publish("act4", ["hong_to_alshire", 3]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: À, mình không có ý gì thô lỗ đâu!

`publish("act4", ["hong_to_alshire", 6]);`

h2: Mình chỉ cần một chút thời gian để xử lý cảm xúc của mình. Làm ơn đừng coi đó là một sự từ chối  nhé.

```
publish("act4", ["hong_to_alshire", 7]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: SUY NGHĨ BỆNH HOẠN NÀO ĐANG ĐIỀU KHIỂN CẬU?! KHAO KHÁT ĐEN TỐI NÀO ĐANG LÁI TRÁI TIM CỦA KẺ TÂM THẦN NÀY?!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: CẬU ĐÃ BỊ TỪ CHỐI! CẬU SẼ KHÔNG BAO GIỜ ĐƯỢC YÊU THƯƠNG!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: CẬU ĐÃ CẮT NGANG QUÁ TRÌNH XỬ LÝ CẢM XÚC CỦA HỌ! GIỜ HỌ SẼ BỊ CHẤN THƯƠNG MÃI MÃI VÀ ĐÓ LÀ LỖI CỦA CẬU!
{{/if}}

(#act4e)

# act4e

```
Game.WORDS_HEIGHT_BOTTOM = 195;
publish("act4", ["alshire", 6]);
```

s: CHẠY CHẠY CHẠY CHẠY CHẠY CHẠY CHẠY CHẠY CHẠY CHẠY CHẠY

```
Game.clearText();
publish("act4", ["hong_to_alshire", 0]);
publish("act4", ["alshire", 10]);
sfx("pop");
```

(...1001)

```
publish("act4", ["alshire", 11]);
sfx("alshire_run");
```

(...2601)

```
publish("act4-out-3");
Game.WORDS_HEIGHT_BOTTOM = -1; /* reset */
```

(...1201)

`publish("act4-jumpcut-hong");`

h: Hả. Thật kỳ lạ. Tớ tự hỏi không biết họ đang nghĩ gì trong đầu.

`publish("act4", ["hong_closer", 2]);`

h: Dù sao, cậu đang nói gì nhỉ?

```
publish("act4", ["hong_closer", 1]);
publish("act4", ["bb_closer", 6]);
```

b: Ờ, tớ quên rồi? Chuyện gì đó về các đội và công việc?

```
publish("act4", ["bb_closer", 0]);
publish("act4", ["hong_closer", 3]);
```

h: ¯\_(ツ)_/¯

```
publish("act4", ["hong_closer", 1]);
publish("act4", ["bb_closer", 4]);
```

b: Họ nói cậu nên "làm hòa" với cảm xúc của mình, như thể cảm xúc của cậu là *tội phạm chiến tranh*.

`publish("act4", ["bb_closer", 7]);`

b: Nhưng tớ muốn chúng ta tạo ra *nhiều* hơn chỉ là hòa bình! Tớ muốn chúng ta trở thành *đồng minh!*

`publish("act4", ["bb_closer", 3]);`

b: Tớ muốn trở thành một con chó canh gác tốt. Giống như đói và khát là những tín hiệu cho nhu cầu thể chất của cậu,

`publish("act4", ["bb_closer", 8]);`

b: Tớ muốn trở thành tín hiệu cho những nhu cầu *tâm lý* của cậu – nhu cầu về sự an toàn, cảm giác thuộc về, và điều tốt đẹp.

`publish("act4", ["bb_closer", 1]);`

b: Nhưng... tớ làm việc này tệ quá, nên tớ cần cậu dạy tớ.

`publish("act4", ["bb_closer", 4]);`

b: Tớ không phải là "luôn hợp lý," cũng không phải là "luôn vô lý." Tớ chỉ đang... cố gắng hết sức. Nên, làm ơn,

`publish("act4", ["bb_closer", 30]);`

b: Hãy giúp tớ giúp cậu!

`publish("act4", ["bb_closer", 6]);`

b: Dù sao, việc dạy một con chó già những mẹo mới *sẽ* mất một thời gian. Có thể *nhiều năm.*

`publish("act4", ["bb_closer", 3]);`

b: Và đôi khi tớ sẽ tái phát, tớ sẽ quay lại những thói quen cũ của mình.

`publish("act4", ["bb_closer", 2]);`

b: Tớ sẽ sủa vào bóng đen. Tớ sẽ làm cậu sợ bằng những lời nói. Tớ thậm chí có thể cho cậu thấy một số hình ảnh xâm phạm về... những thứ.

`publish("act4", ["bb_closer", 9]);`

b: Tớ xin lỗi! Tớ là một con chó  bị tổn thương! Những con chó bị tổn thương đôi khi sẽ ị lên giường của cậu!

`publish("act4", ["bb_closer", 4]);`

b: Nhưng nếu cậu kiên nhẫn với tớ... chỉ cần ở lại, ngồi bên tớ...

`publish("act4", ["bb_closer", 8]);`

b: Cậu có thể thuần hóa con sói này.

`publish("act4", ["bb_closer", 0]);`

`Game.clearText();`

(...1000)

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Chó ngoan.](#act4f-pat-bb) `Game.OVERRIDE_CHOICE_SPEAKER = "h"; publish("act4", ["hong_closer", 2]);`

`Game.OVERRIDE_CHOICE_SPEAKER = "b"`

[Người tốt.](#act4f-pat-hong) `Game.OVERRIDE_CHOICE_SPEAKER = "b"; publish("act4", ["bb_closer", 8]);`

# act4f-pat-hong

```
Game.clearText();
publish("hide_tabs");
Game.FORCE_CANT_SKIP = true;
music(null,{fade:0.5});
sfx("youbothwin");
```

```
publish("act4", ["hong_closer", 4]);
publish("act4", ["bb_closer", 13]);
```

(...501)

`publish("act4", ["bb_closer", 14]);`

(...501)

`publish("act4", ["bb_closer", 13]);`

(...501)

`publish("act4", ["bb_closer", 14]);`

(...501)

`publish("act4", ["bb_closer", 13]);`

(...501)

`publish("act4", ["bb_closer", 14]);`

(...6501)

`publish("act4", ["bb_closer", 15]);`

(...1001)

(#act4f)

# act4f-pat-bb

```
Game.clearText();
publish("hide_tabs");
Game.FORCE_CANT_SKIP = true;
music(null,{fade:0.5});
sfx("youbothwin");
```

```
publish("act4", ["hong_closer", 4]);
publish("act4", ["bb_closer", 10]);
```

(...501)

`publish("act4", ["bb_closer", 11]);`

(...501)

`publish("act4", ["bb_closer", 10]);`

(...501)

`publish("act4", ["bb_closer", 11]);`

(...501)

`publish("act4", ["bb_closer", 10]);`

(...501)

`publish("act4", ["bb_closer", 11]);`

(...6501)

`publish("act4", ["bb_closer", 12]);`

(...1001)

(#act4f)

# act4f

```
Game.FORCE_CANT_SKIP = false;
publish("act4", ["bb_closer", 16]);
publish("act4", ["hong_closer", 5]);
```

{{if _.fifteencigs}}
b: AAAAA CẬU VẪN ĂN MỘT MÌNH MƯỜI NĂM ĐIẾU THUỐC AAAAA
{{/if}}

{{if _.parasite}}
b: AAAAA CẬU VẪN KHÔNG LÀM VIỆC KHI ĂN, CẬU LÀ KÝ SINH TRONG XÃ HỘI AAAAA
{{/if}}

{{if _.whitebread}}
b: AAAAA CẬU ĐANG ĂN NHIỀU BÁNH MÌ TRẮNG HƠN AAAAA
{{/if}}

```
publish("act4", ["bb_closer", 18]);
publish("act4", ["hong_closer", 6]);
sfx("yaps", {volume:0.6});
Game.FORCE_CANT_SKIP = true;
Game.WORDS_HEIGHT_BOTTOM = 205;
Game.FORCE_TEXT_DURATION = 90;
Game.FORCE_NO_VOICE = true;
```

b: GÂU GÂU GÂU GÂU GÂU 

(#credits)
