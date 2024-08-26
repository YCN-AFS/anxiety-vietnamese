# act1

```
SceneSetup.act1();
```

(...300)

n: VÀ ĐÂY LÀ NỖI LO ÂU CỦA CON NGƯỜI

n: _BẠN_ CHÍNH LÀ NỖI LO ÂU

{{if window.localStorage.continueChapter=="replay"}}
(#act1_replay)
{{/if}}

{{if window.localStorage.continueChapter!="replay"}}
(#act1_normal)
{{/if}}



# act1_replay

`hong({mouth:"0_neutral", eyes:"0_neutral"})`

h: Ồ này! Chúng ta lại ở đây nữa sao?

`hong({eyes:"0_neutral"})`

n: NHIỆM VỤ CỦA CẬU LÀ BẢO VỆ CON NGƯỜI CỦA MÌNH KHỎI *NGUY HIỂM*

`bb({eyes:"look", mouth:"small_lock"})`

n: THẬT RA, CHƠI LẠI TRÒ NÀY ĐANG ĐẶT HỌ VÀO *NGUY HIỂM* ĐẤY!

n: NHANH LÊN, CẢNH BÁO HỌ NGAY ĐI!

```
sfx("squeak");
bb({body:"squeeze_talk"});
hong({body:"0_squeeze"});
```

b: Này, con người! Nghe này, chúng ta đang gặp nguy hiểm! Người chơi...

[...cậu lại đến hành hạ mình 1 lần nữa!](#act1_replay_torture)

[...không thể có một kết thúc khác được sao!](#act1_replay_alternate)

[...điều này làm ra xung đột cốt truyện cậu biết chứ!](#act1_replay_dissonance)

# act1_replay_torture

```
window.HACK_REPLAY = JSON.parse(localStorage.act4);
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

{{if window.HACK_REPLAY.act1_ending=="fight"}}
b: Họ sẽ làm chúng ta cuộn tròn lại rồi khóc ròng mất thôi!
{{/if}}

{{if window.HACK_REPLAY.act1_ending=="flight"}}
b: Họ sẽ bắt chúng tôi phải tắt điện thoại của bạn vì nó cậu hoảng loạn đấy!
{{/if}}

{{if window.HACK_REPLAY.a2_ending=="fight"}}
b: Họ sẽ khiến chúng ta *KHÔNG* đấm vào người chủ bữa tiệc!
{{/if}}

{{if window.HACK_REPLAY.a2_ending=="flight"}}
b: Họ sẽ bắt cậu đấm vào mặt người chủ tiệc là nhân vật phản diện đáng thương!
{{/if}}

{{if window.HACK_REPLAY.a3_ending=="jump"}}
h: Ít nhất thì lần này chúng ta có thể sẽ không nhảy khỏi mái nhà--
{{/if}}

{{if window.HACK_REPLAY.a3_ending=="walkaway"}}
b: HỌ SẼ LÀM CHÚNG TA PHẢI NHẢY KHỎI MÁI NHÀ.
{{/if}}

`bb({body:"fear"});`

b: TẤT CẢ NHỮNG ĐIỀU KHỦNG KHIẾP MỚI NÀY SẼ XẢY RA VỚI CHÚNG TA, VÀ SAU ĐÓ CHÚNG TA SẼ--

(#act1_replay_end)


#act1_replay_alternate

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

h: Ừ thì, câu chuyện toàn bộ vẫn giống nhau, nhưng mỗi chương có hai kết thúc khả thi, chưa kể tất cả các lựa chọn đối thoại phân nhánh...--

`bb({body:"fear"});`

b: Người chơi sẽ thất vọng, đóng tab trình duyệt này, xóa phần trò chơi của chúng ta, và rồi chúng ta sẽ--

(#act1_replay_end)


# act1_replay_dissonance

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

h: Cái gì dâm dục cơ?

`bb({eyes:"normal"});`

b: Cốt truyện nói về cách bạn có thể *LỰA CHỌN* xây dựng một mối quan hệ lành mạnh với nỗi sợ của mình,

`bb({eyes:"normal_right"});`

b: Nhưng chơi lại trò chơi sẽ cho cùng một cốt truyện, ngụ ý rằng *LỰA CHỌN* của bạn không quan trọng,

`bb({eyes:"narrow_eyebrow"});`

b: Do đó, điều này cho thấy sự mâu thuẫn giữa thông điệp và cơ chế của trò chơi,

`bb({eyes:"fear"});`

b: Do đó, làm tan rã cấu trúc của vũ trụ câu chuyện này,

`bb({body:"fear"});`

b: Và rồi chúng ta sẽ--

(#act1_replay_end)


# act1_replay_end

`bb({body:"panic"})`

b: CHẾTTTTTTTTTTTTTTTTTTTTT

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.clearText();
```

(...1001)

```
bb({body:"laugh"});
hong({body:"laugh"});
Game.clearText();
sfx("laugh");
```

(...5001)

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({body:"0_sammich"});
```

h: Được rồi, nhập tâm vào nhân vật nào.

```
Game.clearText();
```

n4: (HÃY ĐỂ SỰ LO LẮNG CỦA _BẠN_ BLAH BLAH BLAH GIỐNG NHẤT VỚI SỰ SỢ HÃI CỦA _BẠN_ BLAH BLAH BẠN BIẾT RỒI MÀ)

```
sfx("squeak");
hong({body:"0_squeeze"});
bb({body:"squeeze"});
```

(#act1_normal_choice)



# act1_normal

`hong({mouth:"0_neutral", eyes:"0_annoyed"})`

h: Ôi tốt quá, con sói của mình đã trở lại. Tuyệeeet vời thật.

`hong({eyes:"0_neutral"})`

n: BẠN CẦN BẢO VỆ BẢN THÂN MÌNH KHỎI *NGUY HIỂM*

`bb({eyes:"look", mouth:"small_lock"})`

n: THỰC TẾ, CHIẾC SANDWICH ĐÓ ĐANG ĐẶT BẠN VÀO *NGUY HIỂM* NGAY BÂY GIỜ

n: NHANH NÀO, HÃY CẢNH BÁO BẢN THÂN!

```
sfx("squeak");
bb({body:"squeeze_talk"});
hong({body:"0_squeeze"});
```

b: Con người! Nghe này, chúng ta đang gặp nguy hiểm! Mối nguy là...

`bb({body:"squeeze"})`

n4: (HÃY ĐỂ SỰ LO LẮNG CỦA _BẠN_ BẮT ĐẦU! CHỌN ĐIỀU GIỐNG NHẤT VỚI NHỮNG GÌ NỖI SỢ HÃI CỦA _BẠN_ NÓI VỚI BẠN)

(#act1_normal_choice)

# act1_normal_choice

[Cậu lại ăn trưa một mình! Một lần nữa!](#act1a_alone) `bb({body:"squeeze_talk"})`

[Cậu không thể làm việc hiệu quả khi ăn được!](#act1a_productive) `bb({body:"squeeze_talk"})`

[Ăn bánh mì trắng không tốt cho cậu!](#act1a_bread) `bb({body:"squeeze_talk"})`

# act1a_alone

```
bb({body:"normal", mouth:"small", eyes:"narrow"});
hong({body:"0_sammich"});
```

b: Cậu không biết rằng sự cô đơn có liên quan đến cái chết sớm ngang với việc hút 15 điếu thuốc mỗi ngày sao?-

`Game.OVERRIDE_TEXT_SPEED = 2;`

`bb({mouth:"normal", eyes:"normal_right"})`

b: (Nguồn: Holt-Lunstad 2010, PLoS Medicine)

`hong({eyes:"0_annoyed"})`

h: Ừm, cảm ơn cậu đã trích dẫn nguồn nhưng--

`Game.OVERRIDE_TEXT_SPEED = 2;`

`bb({body:"fear", mouth:"normal", eyes:"fear"})`

b: Điều đó có nghĩa là nếu cậu không đi chơi với ai đó *ngay bây giờ* thì cậu sẽ-

`bb({body:"panic"})`

b: CHẾTTTTTTTTTTTTTTTTTTTTT

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "alone");
publish("hp_show");
```

(...2500)

`_.fifteencigs = true`

n: BẠN ĐÃ SỬ DỤNG *NỖI SỢ KHÔNG ĐƯỢC YÊU THƯƠNG*

(#act1b)

# act1a_productive

```
bb({body:"normal", mouth:"small", eyes:"normal"});
hong({body:"0_sammich"});
```

b: Hãy lấy laptop ra và bắt đầu làm việc ngay bây giờ!

`hong({eyes:"0_annoyed"})`

h: Hừmm, mình không muốn có vụn bánh mì rơi vào bàn phím--

```
bb({mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Nếu không đóng góp cho xã hội thì cậu chả khác gì một kẻ ăn bám xã hội cả!

b: Xã hội này giống như một cơ thể, các "tế bào miễn dịch" sẽ tìm kiếm và đào thải những kẻ ăn bám, và khi đó cậu sẽ--

```
bb({body:"panic", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: CHẾTTTTTTTTTTTTTTTTTTTTT

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "bad");
publish("hp_show");
```

(...2500)

`_.parasite = true`

n: BẠN ĐÃ SỬ DỤNG *NỖI SỢ TRỞ THÀNH NGƯỜI XẤU*

(#act1b)

# act1a_bread

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich", eyes:"0_annoyed"});
```

h: Nghiên cứu đó đã được kiểm chứng chưa--

```
bb({body:"fear", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Ăn lúa mì đã qua chế biến sẽ làm tăng lượng đường trong máu dẫn tới việc cậu phải cắt cụt chi và sau đó cậu sẽ-

`bb({body:"panic"})`

b: CHẾTTTTTTTTTTTTTTTTTTTTT

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "harm");
publish("hp_show");
```

(...2500)

`_.whitebread = true`

n: BẠN ĐÃ SỬ DỤNG *SỢ BỊ TỔN THƯƠNG*

(#act1b)

# act1b

n: NÓ CÓ HIỆU QUẢ SIÊU CẤP

`bb({mouth:"smile", eyes:"smile"});`

b: Thấy chưa, con người? Tớ là chú sói bảo vệ trung thành của cậu!

`bb({body:"pride_talk"});`

b: Hãy tin vào trực giác của cậu! Cảm xúc của cậu luôn luôn đúng!

`bb({body:"pride"});`

n: LÀM CHO THANH NĂNG LƯỢNG CỦA CON NGƯỜI VỀ CON SỐ 0

n: ĐỂ BẢO VỆ NHU CẦU VỀ THỂ CHẤT + XÃ HỘI + ĐẠO ĐỨC, BẠN CÓ THỂ SỬ DỤNG:

n: SỢ *BỊ TỔN THƯƠNG* #harm#

n: SỢ *KHÔNG ĐƯỢC YÊU THƯƠNG* #alone#

n: VÀ SỢ *TRỞ THÀNH NGƯỜI XẤU* #bad#

`Game.OVERRIDE_TEXT_SPEED = 1.25;`

n4: (MẸO HAY: HÃY TÌM NHỮNG LỰA CHỌN ĐÁNH VÀO NỖI SỢ HÃI SÂU SẮC NHẤT CỦA BẠN!~)

h: ...

```
hong({body:"putaway"});
sfx("rustle");
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

(...1000)

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

h: Cậu biết không, có lẽ đã đến lúc mình nên kiểm tra điện thoại rồi.

```
sfx("rustle2");
hong({body:"phone1", mouth:"neutral", eyes:"neutral"})
```

n: HÃY BẢO VỆ CON NGƯỜI CỦA BẠN

n: KHỎI THẾ GIỚI. KHỎI NGƯỜI KHÁC. VÀ KHỎI CHÍNH HỌ.

n: CHÚC MAY MẮN

(...500)

`Game.clearText()`

(...500)

(#act1c)

# act1c

`music('battle', {volume:0.5})`

n: HIỆP MỘT: *BẮT ĐẦU!*

`bb({body:"normal", mouth:"normal", eyes:"normal"});`

h: Hửm. Trên Facebook thông báo là có một bữa tiệc diễn ra vào cuối tuần này.

`bb({eyes:"uncertain"});`

b: Chẳng phải cái gã lập dị đó tổ chức tiệc *mỗi* tuần sao?

`bb({eyes:"uncertain_right"});`

b: Có phải họ đang cố lấp đầy khoảng trống trong tâm hồn? Chắc hẳn họ đang có vấn đề về tâm lý!

`hong({eyes:"surprise"});`

h: Mà, mình cũng được mời?

`bb({eyes:"fear", mouth:"normal"});`

b: Ồ, vậy à!

[Đồng ý đi, nếu không cậu sẽ chết vì cô đơn!](#act1c_loner)

[Hãy từ chối, đồ ăn có thể có độc!](#act1c_drugs)

[Hãy bỏ qua nó đi, cậu chỉ làm cho bữa tiệc mất vui thôi.](#act1c_sad)

# act1c_loner

{{if _.fifteencigs}}
b: Mười lăm điếu thuốc một ngày, con người ạ! Mười lăm!
{{/if}}

{{if !_.fifteencigs}}
`Game.OVERRIDE_TEXT_SPEED = 1.5;`
{{/if}}

{{if !_.fifteencigs}}
b: Nếu từ chối, cậu sẽ chết trong cô đơn và xác cậu sẽ bị vứt ra đường QUẠ rỉa thịt,
{{/if}}

{{if !_.fifteencigs}}
b: và cậu sẽ trở thành PHÂN QUẠ!
{{/if}}

{{if !_.fifteencigs}} `_.whalepoop = true` {{/if}}

(...500)

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`bb({eyes:"normal"});`

{{if !_.fifteencigs}}
b: Vậy có lẽ mình sẽ đi đến bữa tiệc đó!
{{/if}}

{{if _.parasite}}
b: Mình cần mang theo máy tính xách tay để có thể làm việc, và không trở thành kẻ ăn bám của xã hội.
{{/if}}

{{if _.whitebread}}
b: Miễn là họ không tiếp đã mình bằng BÁNH MÌ TRẮNG
{{/if}}

`hong({mouth:"anger", eyes:"anger"});`

h: ^CON MẸ NÓ^, cậu có thể  ^ngậm miệng^ lại được không? Mình ổn.

h: Mình sẽ tham gia bữa tiệc..

{{if _.whalepoop}}
b: Phân quạ, con người! Đừng để chết trong cô đơn!
{{/if}}

`_.partyinvite="yes"`

(#act1d)

# act1c_drugs

`bb({mouth:"small", eyes:"fear"});`

{{if _.whitebread}}
b: hoặc thậm chí tệ hơn... BÁNH MÌ TRẮNG
{{/if}}

{{if _.whitebread}}
`Game.OVERRIDE_TEXT_SPEED = 1.5;`
{{/if}}

{{if _.whitebread}}
b: Cậu ăn quá nhiều bánh mì trắng đến mức khi chết người ta không thể nhét cái xác béo ú của cậu vào lò hỏa táng!
{{/if}}

{{if !_.whitebread}}
b: Cậu có thể dùng thuốc quá liều đến nỗi người quản lý tang lễ sẽ tự hỏi làm sao cơ thể cậu *đã* được ướp xác trước!
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

{{if _.parasite}}
b:  Hơn nữa, không thể tiệc tùng mãi được, cậu cần phải làm việc, nếu không thì cậu sẽ trở thành những kẻ sống bám vào xã hội!
{{/if}}

`hong({mouth:"anger", eyes:"anger"});`

h: ĐỦ RỒI. Mình sẽ làm mọi thứ miễn khiến cậu ngậm miệng lại.

h: Mình từ chối được chưa.

`_.partyinvite="no"`

(#act1d)

# act1c_sad

`bb({eyes:"uncertain_right", mouth:"normal"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

{{if _.fifteencigs}}
b: Những gì cậu nên làm là ngồi khóc trong góc về sự cô đơn nguy hiểm như việc hút 15 điếu thuốc mỗi ngày vậy.
{{/if}}

{{if _.parasite}}
b: Trong buổi tiệc, điều duy nhất cậu cần lo là làm sao để có thể làm việc hiệu quả.
{{/if}}

{{if _.whitebread}}
b: Tất cả những gì cậu cần làm là lo lắng về việc những lựa chọn thực phẩm không lành mạnh sẽ giết chết cậu.
{{/if}}

```
bb({mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"lookaway"});
```

h: ôi trời, tớ tự hỏi tại sao.

`hong({eyes:"neutral"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

b: Vậy nếu cậu đi thì họ sẽ cảm thấy không vui, nhưng nếu cậu từ chối lời mời của họ thì họ cũng sẽ cảm không vui.

`bb({body:"fear", eyes:"fear"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

b: TẤT CẢ NHỮNG GÌ CẬU LÀM LÀ LÀM MỌI NGƯỜI CẢM THẤY KHÔNG VUI, VÌ VẬY CẬU NÊN CẢM THẤY TỘI LỖI VÌ NHỮNG GÌ CẬU LÀM

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

`hong({mouth:"anger", eyes:"anger"});`

h: ĐỦ RỒI. Mình sẽ làm mọi thứ miễn khiến cậu ngậm miệng lại.

h: Mình từ chối được chưa.

`_.partyinvite="ignore"`

(#act1d)

# act1d

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"annoyed"});
```

h: Dù sao thì, mình lướt Faceboọk nhiều quá. Mình cần tìm thứ gì đó để chữa lành và ít tiêu cực hơn.

`hong({eyes:"neutral"});`

h: Có gì hay trên Tiktok không nhỉ?

`bb({eyes:"look"});`

[Trời ơi, xem cái video kia mà sởn cả gai ốc!](#act1d_news)

[Trời ơi, cái video đó đang nói về *mình* sao?](#act1d_subtweet)

[Ơ kìa,video về một chú mèo đang uống sữa.](#act1d_milk)


# act1d_news

```
bb({eyes:"pained1"});
music(null, {fade:2});
```

b: Trời ơi, mình cảm giác như cả thế giới đang chống lại mình vậy?

```
bb({eyes:"pained2"});
hong({mouth:"sad", eyes:"sad"});
```

b: Cảm giác như mọi thứ đang kết thúc, mọi thứ như đang chết dần và số phận cậu đã bị định sẵn, không thể làm gì để thay đổi.

```
Game.OVERRIDE_TEXT_SPEED = 0.5;
bb({mouth:"shut"});
```

b: ...

`bb({mouth:"smile", eyes:"smile"});`

b: Cậu chia sẻ lại nội dung tiêu cực này nhé!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

`_.badnews=true`

```
music('battle', {volume:0.5});
hong({mouth:"anger", eyes:"anger"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Được rồi mình chia sẻ, nhưng im lặng giùm mình được không?

`hong({mouth:"neutral", eyes:"annoyed"});`

h: Thôi kệ, mình xem trên Twitter có gì đã.

(#act1e)


# act1d_subtweet

`bb({eyes:"fear"});`

b: Đây là bài viết ẩn, một bài viết chứa đầy ấn ý!

`hong({eyes:"annoyed"});`

h: Có lẽ là không?

`bb({eyes:"narrow", mouth:"small"});`

b: nhưng nếu họ đang nói xấu sau lưng cậu thì sao

h: Mình nghĩ à họ khô--

`bb({body:"fear", eyes:"fear", mouth:"normal"});`

b: NÓI XẤU NGAY TRƯỚC MẶT CẬU

`hong({eyes:"sad", mouth:"sad"});`

h: mình không--

`bb({eyes:"narrow", mouth:"small"});`

b: nhưng *nếu như* thì sao

h: Dừng l--

`bb({eyes:"narrow_eyebrow"});`

b: *nếu như*

```
Game.OVERRIDE_TEXT_SPEED = 0.5;
hong({mouth:"shut"});
```

h: ...

(...1000)

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`_.subtweet=true`

```
hong({mouth:"anger", eyes:"annoyed"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: Thôi rồi, mình sẽ thử Snapchat.

(#act1e)

# act1d_milk

`hong({mouth:"smile", eyes:"neutral"});`

h: Heh ya dễ thương quá, mình vừa mới trả lời lại, mình nghĩ--

```
hong({mouth:"shock", eyes:"shock"});
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.8;
```

b: MÈO KHÔNG THỂ TIÊU HÓA SỮA VÀ CẬU LÀ KẺ TỆ BẠI VÌ THÍCH THÚ VỚI VIỆC NGƯỢC ĐÃI ĐỘNG VẬT

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
attack("18p", "bad");
```

(...2500)


`_.catmilk=true`

```
hong({mouth:"anger", eyes:"annoyed"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: Được thôi, mình sẽ thử Snapchat.

(#act1e)

# act1e

`hong({mouth:"neutral", eyes:"neutral"});`

h: Hả? Bức ảnh chụp vào tối qua. Vậy *hóa ra* cái thằng đó tuần nào cũng mở tiệc.

{{if _.partyinvite=="yes"}} (#act1e_said_yes) {{/if}}

{{if _.partyinvite=="no"}} (#act1e_said_no) {{/if}}

{{if _.partyinvite=="ignore"}} (#act1e_said_ignore) {{/if}}

# act1e_said_yes

`hong({mouth:"sad", eyes:"annoyed"});`

h: Ôi, ở đó đông người quá, mình cảm thấy không ổn khi đến nơi như vậy.

h: Có lẽ mình nên từ chối lời mời này?

```
hong({mouth:"neutral", eyes:"neutral"});
bb({mouth:"normal", eyes:"normal"});
```

[Đổi ý ư? Cậu khùng hả?!](#act1e_yes_dontchange)

[Từ chối đi! Ở đó đông đúc quá!](#act1e_yes_changetono)

{{if _.subtweet}}
[Đúng là họ đang ngầm ám chỉ cậu.](#act1e_ignore_subtweet)
{{/if}}

{{if _.badnews}}
[Khoan đã, cậu đăng lại bữa tiệc mà không kiểm tra...](#act1e_ignore_factcheck)
{{/if}}

{{if (!_.subtweet && !_.badnews)}}
[Cậu biết không, tư thế của cậu thực sự tệ phải không?](#act1e_ignore_posture)
{{/if}}

# act1e_yes_dontchange

```
bb({eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Bọn họ mong chờ cậu đến và giờ cậu phản bội lòng tin của họ? Cậu chết trong cô đơn sao?!

{{if _.fifteencigs}}
b: MƯỜI NĂM ĐIẾU THUỐC LÁ.
{{/if}}

{{if _.whalepoop}}
b: WHALE. POOP.
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

```
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Thôi mà thôi mà, tớ đồng ý!

(#act1f)

# act1e_yes_changetono

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Cậu không biết về những vụ giẫm đạp của tại những nơi đông người à?

```
bb({body:"fear", mouth:"small", eyes:"narrow"});
hong({eyes:"sad", mouth:"sad"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Vào năm 2022, một đám đông người dân đi dự lễ Halloween ở Itaewon, Hàn Quốc đã tràn vào một con hẻm hẹp, gây ra vụ giẫm đạp khiến hơn 150 người thiệt mạng--

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({mouth:"shock"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: CẬU CÓ MUỐN ĐIỀU ĐÓ XẢY RA VỚI CHÍNH CẬU KHÔNG-

```
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 2.5;
```

b: TỪ CHỐI ĐI! TỪ CHỐI ĐI! TỪ CHỐI ĐI! TỪ CHỐI ĐI! TỪ CHỐI ĐI! TỪ CHỐI ĐI! TỪ CHỐI-


```
bb({body:"normal", eyes:"fear", mouth:"normal"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

```
hong({eyes:"anger", mouth:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Im đi, im đi, tớ sẽ đổi câu trả lời thành không! Trời ơi!

(#act1f)

# act1e_said_no

`hong({mouth:"sad", eyes:"sad"});`

h: Ừm... trông vui thật đấy.

h: Có lẽ mình không nên từ chối lời mời?

`bb({mouth:"normal", eyes:"normal"});`

[Cậu định đổi ý à? Hèn thật!](#act1e_no_dontchange)

[Đổi ý đi! Đừng chết trong cô đơn.](#act1e_no_changetoyes)

{{if _.subtweet}}
[Yeah, đúng là họ đang ngầm ám chỉ cậu.](#act1e_ignore_subtweet)
{{/if}}

{{if _.badnews}}
[Chờ đã, cậu chia sẻ lại mà không kiểm tra thông tin.](#act1e_ignore_factcheck)
{{/if}}

{{if (!_.subtweet && !_.badnews)}}
[Cậu biết không, tư thế của cậu thật sự rất tệ đó!](#act1e_ignore_posture)
{{/if}}

# act1e_no_dontchange

`bb({eyes:"anger"})`

b: Mọi người đều trông chờ vào cậu!

b: ...để họ yên và cho họ có một bữa tiệc vui vẻ mà không bị làm phiền bởi những thứ kinh khủng, ghê tởm {{if _.whitebread}}white-bread-munching{{/if}} giống như cậu--


```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

```
bb({body:"normal", eyes:"uncertain", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Im đi, im đi,  câu trả lời của mình vẫn sẽ là không!

(#act1f)

# act1e_no_changetoyes

```
bb({body:"fear", eyes:"fear", mouth:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Sự cô đơn kéo dài làm tăng mức cortisol cũng như nguy cơ mắc bệnh tim mạch và đột quỵ!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

{{if _.fifteencigs}}
b: FIFTEEN. CIGARETTES.
{{/if}}

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Ngậm miệng lại đi giùm đi! Mình sẽ đồng ý! Trời ơi!

(#act1f)

# act1e_ignore_subtweet

```
bb({eyes:"fear", mouth:"small"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Tất cả những gì cậu chia sẻ sẽ gây rắc rối cho cậu, và chúng đã quay trở lại để cậu lĩnh lấy hậu quả!

```
bb({body:"fear", eyes:"fear", mouth:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.7;
```

b: Cậu sẽ bị chỉ trích, bị tẩy chay, và bị buộc vào dây thừng và bị ngựa kéo lê tới ^chết^ , nhưng mà ở trên internet.

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Tại sao cậu lại như thế này?!

(#act1f)

# act1e_ignore_factcheck

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Cậu đang lan truyền thông tin sai lệch! Cậu đang phá hoại niềm tin vào nền báo chí tự do!

```
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Cậu chính là lý do khiến chủ nghĩa phát xít sẽ trỗi dậy từ đống đổ nát của nền dân chủ!

```
bb({body:"normal", eyes:"anger"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

```
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
_.factcheck = true;
```

h: Tại sao cậu lại như thế này?!

(#act1f)

# act1e_ignore_posture

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Cậu muốn lưng còng như bánh quẩy à?! Ngồi thẳng lưng lên, đừng cúi gập vào màn hình nữa!

```
bb({body:"meta"});
```

b: Cái này cũng áp dụng cho cậu đấy.

```
bb({body:"normal", mouth:"normal"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Sao cậu lại như thế này?!

(#act1f)

# act1e_said_ignore

`hong({mouth:"sad", eyes:"sad"});`

h: Ừm... trông vui thật đấy.

h: Có lẽ mình không nên từ chối lời mời đó?

`bb({mouth:"normal", eyes:"normal"});`

[Cứ lờ đi, cậu vẫn là kẻ phá đám ở buổi tiệc thôi.](#act1e_ignore_continue)

[Thực ra, hãy đồng ý.](#act1e_ignore_changetoyes)

[Thực ra, hãy từ chối.](#act1e_ignore_changetono)

# act1e_ignore_continue

`hong({eyes:"annoyed"});`

h: Nhưng cứ lờ họ đi thì cũng hơi bất lịch sự, đúng không?

`bb({eyes:"normal_right"});`

b: Hmm, những người khác luôn phớt lờ *cậu*, vì vậy

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`bb({eyes:"normal"});`

b: vậy thì cậu cứ coi như hòa nhé.

(#act1f)

# act1e_ignore_changetoyes

`hong({eyes:"surprise", mouth:"smile"});`

h: Ủa... cậu... đang để mình vui chơi thoải mái à?

b: À, ý mình là, cô đơn cũng *có thể* giết chết cậu mà.

`hong({eyes:"neutral", mouth:"neutral"});`

(#act1e_no_changetoyes)

# act1e_ignore_changetono

`bb({eyes:"narrow"});`

b: Đông quá. Đám đông thật nguy hiểm.

(#act1e_yes_changetono)


# act1f

```
hong({mouth:"neutral", eyes:"neutral"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: Kệ nó đi. Trên Tinder có thông báo mới.

`bb({eyes:"uncertain"})`

b: Gì cơ? Cái ứng dụng hẹn hò đó à?

`hong({eyes:"annoyed"})`

h: Đây không hẳn là app hẹn hò, nó là nơi cậu có thể gặp những con người mới--

`bb({eyes:"narrow"})`

b: Đây rõ ràng là ứng dụng hẹn hò.

```
hong({eyes:"surprise", mouth:"smile"});
bb({eyes:"normal"});
```

h: Ơ này, tớ vừa được ghép đôi với ai đó, cậu ấy trông thật dễ thương.

```
bb({eyes:"narrow_eyebrow"});
hong({eyes:"sad", mouth:"anger"})
```

h: Đừng làm hỏng chuyện của tớ--

```
bb({body:"panic"});
Game.OVERRIDE_TEXT_SPEED = 2.0;
```

b: NGUY HIỂM - NGUY HIỂM - THẬT NGUY HIỂM

`bb({body:"fear", eyes:"fear", mouth:"normal"})`

[Cậu chỉ đang bị người khác *lợi dụng* thôi.](#act1f_used_by_others)

[Cậu chỉ đang *lợi dụng* người ta thôi.](#act1f_using_others)

[CẬU ĐANG GHÉP ĐÔI VỚI SÁT NHÂN HÀNG LOẠT](#act1f_killer)

# act1f_used_by_others

`bb({body:"point_crotch", eyes:"normal", mouth:"normal"})`

b: Những cuộc gặp gỡ với người xa lạ có thể lấp đầy khoảng trống trong lòng cậu,

b: nhưng chúng không bao giờ thỏa mãn được con quỷ cô đơn...

`bb({body:"point_heart", eyes:"pretty", mouth:"small"})`

b: ở *trong tim cậu*.

(...1000)

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Vấn đề ở đây là CẬU SẼ CHẾT TRONG CÔ ĐƠN

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`_.hookuphole=true`

(#act1g)

# act1f_using_others

`bb({eyes:"narrow", mouth:"small"})`

b: Cậu nghĩ ^bộ phận sinh dục^ của người khác là Pokémon để cậu sưu tầm à?

```
bb({body:"sing", eyes:"pretty", mouth:"shut"});
music("pokemon");
Game.clearText();
Game.FORCE_CANT_SKIP = true;
```

```
Game.FORCE_TEXT_DURATION = 1000;
Game.FORCE_NO_VOICE = true;
```

b: ♫ (bài hát chủ đề pokemon)-

(...5600)

```
bb({mouth:"normal"});
Game.FORCE_TEXT_DURATION = 2400;
```

b: ♫ Tôi muốn trở thành một  ^con đĩ lẳng lơ^ ... nhất-

(...500)

```
bb({eyes:"narrow", mouth:"small"});
Game.FORCE_TEXT_DURATION = 2100;
```

b: ♫ Như chưa ai từng có-

(...1500)

```
bb({eyes:"pretty"});
Game.FORCE_TEXT_DURATION = 2300;
```

b: ♫ Đùi và ^mông^, ngực căng đầy-

(...500)

```
bb({eyes:"fear", mouth:"normal"});
Game.FORCE_TEXT_DURATION = 2000;
```

b: ♫ với ^con cu^ và hai hòn bi ướt đẫm mồ hôi!-

(...1000)

```
bb({eyes:"smile", mouth:"smile"});
Game.FORCE_TEXT_DURATION = 1000;
```

b: ♫ KẺ BIẾN THÁI! PHẢI BẮT-

```
Game.FORCE_CANT_SKIP = false;
Game.clearText();
music(false);
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Ý là cậu là kẻ thao túng và biến thái.

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

`_.pokemon=true`

(#act1g)

# act1f_killer

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

{{if _.whitebread}}
b: Họ sẽ nhốt cậu xuống giếng rồi ép ăn bánh mì trắng cho mập lên để họ có thể lấy mặc da của cậu để may đồ!
{{/if}}

{{if _.parasite}}
b: Họ sẽ lấy đồng hồ Pomodoro đập vào cậu và hét lên "ĐÁNG RA MÀY NÊN LÀM VIỆC CHĂM CHỈ HƠN ĐỒ ĂN BÁM!"
{{/if}}

{{if !_.whitebread && !_.parasite}}
b: Họ sẽ xé xác cậu thành nhiều mảnh, biến ruột gan thành dây trang trí, và đùng máu cậu để pha với rượu!
{{/if}}

{{if !_.whitebread && !_.parasite}}
b: Thế đã ĐỦ làm thiệp mời dự tiệc chưa?!
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

`_.serialkiller=true`

(#act1g)

# act1g

```
bb({body:"normal", mouth:"normal", eyes:"look"});
hong({body:"2_tired"});
Game.OVERRIDE_TEXT_SPEED = 0.5;
music(false);
```

h: ...

(...500)

h: Mình chán ngấy cái trò chơi này quá rồi.

(...700)

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

h:
{{if _.fifteencigs}}"sự cô đơn đang giết chết tớ"... {{/if}}
{{if _.parasite}}"we're a society-parasite"... {{/if}}
{{if _.whitebread}}"don't eat that, it'll kill us"... {{/if}}
{{if _.subtweet}}"they're talking behind our back"... {{/if}}
{{if _.badnews}}"thế giới như muốn sụp đổ"... {{/if}}
{{if _.hookuphole}}"tớ sẽ chết trong cô đơn"... {{/if}}
{{if _.serialkiller}}"cậu ấy kẻ giết người hàng loạt"... {{/if}}
{{if _.catmilk}}"mèo không thể tiêu hóa sữa"... {{/if}}
{{if _.pokemon}}một bài hát nhại ^dở tệ^..{{/if}}

h: tớ chỉ muốn sống cuộc đời của riêng mình.

h: tớ chỉ muốn thoát khỏi tất cả những đau khổ này.

`bb({eyes:"look_sad"});`

b: Này... con người...

`Game.OVERRIDE_TEXT_SPEED = 0.5;`

b: Mọi thứ rồi cũng sẽ ổn thôi.

(...600)

`bb({body:"point_heart", eyes:"look_sad_smile", mouth:"smile"});`

b: Là chú sói bảo vệ trung thành của cậu, mình sẽ luôn cảnh giác với các mối nguy và cố gắng hết sức để giữ cậu được an toàn.

`bb({body:"normal", eyes:"look_sad", mouth:"smile"});`

b: Mình hứa.

(...600)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({body:"phone1", eyes:"neutral", mouth:"neutral"});
```

h: App cuối cùng. Instagram. Xem thử nó có gì nào?

`hong({eyes:"sad"});`

h: Đây là... lại thêm nhiều ảnh buổi tiệc nữa.

`hong({mouth:"sad"});`

h: Mọi người trông thật vui vẻ. Không lo lắng, không sợ hãi.

`hong({mouth:"anger"});`

h: Trời ơi, tại sao mình không thể giống họ? Tại sao mình không thể *bình thường* như họ?

`bb({eyes:"normal_right"});`

b: Nói về buổi tiệc cuối tuần, theo quyết định CUỐI CÙNG của mình:

`bb({eyes:"normal"});`

[Cậu nên đi.](#act1g_go) `Game.OVERRIDE_CHOICE_LINE=true`

[Cậu nên từ chối.](#act1g_dont) `Game.OVERRIDE_CHOICE_LINE=true`

# act1g_go

`_.act1g = "go"`

(#act1h)

# act1g_dont

`_.act1g = "dont"`

(#act1h)

# act1h

b: Cậu nên--

```
bb({eyes:"wat", mouth:"small"});
hong({body:"2_fuck"});
```

h: *^Đ!T CON MẸ^.*

`hong({body:"2_you"});`

h: NÓ.

(...500)

b: sa

(...1500)

`bb({eyes:"wat_2"});`

b: sao vâ?

`hong({body:"phone1", eyes:"anger", mouth:"anger"});`

h: Mình sẽ THAM GIA buổi tiệc,

{{if _.act1g=="go"}}
h: KHÔNG PHẢI vì cậu muốn mình làm vậy, mà là vì *bản thân* mình muốn làm điều đó.
{{/if}}

{{if _.act1g=="dont"}}
h: Chính là *BỞI VÌ* cậu không muốn tớ làm thế.
{{/if}}

```
hong({body:"putaway"});
sfx("rustle");
```

h: Cậu KHÔNG THỂ kiểm soát được mình.

```
sfx("rustle2");
hong({body:"0_sammich", eyes:"0_annoyed", mouth:"0_neutral"});
```

h: Giờ xin phép để mình thưởng thức chiếc sandwich ngon tuyệt này trong yên bình.

`hong({body:"2_sammich_eat"});`

(...601)

```
sfx("sandwich");
hong({body:"2_sammich_eaten", eyes:"0_lookaway", mouth:"0_chew1"})
```

(...601)

```
bb({body:"normal", eyes:"uncertain", mouth:"shut"});
Game.OVERRIDE_TEXT_SPEED = 0.5;
```

b: ...

```
bb({eyes:"normal_right"});
Game.OVERRIDE_TEXT_SPEED = 1;
```

b: ...

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 4;
```

b: ..................

(...500)

`bb({mouth:"normal"});`

[AHHHH CẬU SẼ CHẾT MẤT](#act1h_death) `Game.OVERRIDE_CHOICE_LINE = true;`

[AHHHH MỌI NGƯỜI ĐỀU GHÉT CẬU](#act1h_loneliness) `Game.OVERRIDE_CHOICE_LINE = true;`

[AHHHH CẬU LÀ MỘT KẺ THẬT TỆ HẠI](#act1h_worthless) `Game.OVERRIDE_CHOICE_LINE = true;`

# act1h_death

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: AHHHH CẬU SẼ CHẾT MẤT AAAAAAHHHHHHH

```
hong({body:"3_defeated1"});
attack("100p", "harm");
```

(...2500)

(#act1i)

# act1h_loneliness

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: AHHHH MỌI NGƯỜI ĐỀU GHÉT CẬU AAAAAAHHHHHHH

```
hong({body:"3_defeated1"});
attack("100p", "alone");
```

(...2500)

(#act1i)

# act1h_worthless

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: AHHHH CẬU LÀ MỘT KẺ THẬT TỆ HẠI AAAAAAHHHHHHH

```
hong({body:"3_defeated1"});
attack("100p", "bad");
```

(...2500)

(#act1i)

# act1i

```
bb({mouth:"smile_lock", eyes:"smile", body:"normal"});
music('battle', {volume:0.5});
```

n: CHÚC MỪNG

(...500)

n: BẠN ĐÃ BẢO VỆ BẢN THÂN THÀNH CÔNG KHỎI NHU CẦU VỀ THỂ CHẤT + XÃ HỘI + ĐẠO ĐỨC CỦA CON NGƯỜI

n: TẠI SAO Ư? NHÌN XEM HỌ BIẾT ƠN NHƯ THẾ NÀO KÌA!

(...500)

n: BÂY GIỜ NĂNG LƯỢNG CỦA HỌ ĐÃ BẰNG KHÔNG, BẠN CÓ THỂ KIỂM SOÁT HÀNH ĐỘNG CỦA HỌ

`bb({mouth:"smile", eyes:"normal"});`

n: CHỌN HÀNH ĐỘNG ĂN MỪNG CỦA BẠN

`bb({mouth:"small_lock", eyes:"fear"});`

n: *ĐÒN KẾT LIỄU*

[{Trừng phạt chiếc điện thoại làm bạn buồn!}](#act1i_phone) `Game.OVERRIDE_CHOICE_LINE=true`

[{Cuộn tròn lại và khóc!}](#act1i_cry) `Game.OVERRIDE_CHOICE_LINE=true`

# act1i_phone

`bb({mouth:"normal", eyes:"narrow"})`

b: Cái điện thoại đang làm cho cậu xuống tinh thần!

`bb({eyes:"anger"})`

b: Zuckerberg và đồng bọn đang bào mòn sức khỏe tinh thần cậu để kiếm tiền của các nhà đầu tư mạo hiểm!

```
bb({body:"fear", eyes:"fear"});
hong({body:"3_defeated2"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Trừng phạt điện thoại của cậu! Phá nó! Đập nó đi!

```
Game.OVERRIDE_TEXT_SPEED = 2.5;
bb({body:"flail"});
hong({body:"3_defeated3"});
_.act1_ending = "fight";
```

b: ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP ĐIỆN THOẠI ĐẬP NÓ ĐI--

(#act1j)

# act1i_cry

`bb({eyes:"fear", mouth:"normal"})`

b: Cả thế giới này đầy rẫy nguy hiểm!

```
bb({body:"fear"});
hong({body:"3_defeated2"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Hãy làm như con tatu! Cuộn tròn lại thành một quả bóng để tự vệ!

```
Game.OVERRIDE_TEXT_SPEED = 2.5;
bb({body:"flail"});
hong({body:"3_defeated3"});
_.act1_ending = "flight";
```

b: CUỘN TRÒN LẠI VÀ KHÓC CUỘN TRÒN LẠI VÀ KHÓC CUỘN TRÒN LẠI VÀ KHÓC CUỘN TRÒN LẠI VÀ-- 

(#act1j)

# act1j

`SceneSetup.act1_outro()`