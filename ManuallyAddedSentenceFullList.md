16 Formosan Languages Sentences That Need to be Manually Added 

Paiwan
delete: [1.valjulu= 咬人樹 
delete: aicu a pinaka vavauan a dredretan papizuanan tua sinan paravac a zaljum ( vava  
delete:  師教導的。
delete: nu pangtjezan timadju nua kinamalji siveric a nemang pasa kasasavan. 只要 他生氣就會把屋內的東西向 

add:  (some are after (.... ) (... .) and some are because of wacky format like 。.)  
PROBLEM: the (... .) are transcribed with current code but (.... ) is not. And the regular expression is not taking r"\.{4}\s*" for some reason. So the sentences are still being manually added 

add: nu pangtjezan timadju nua kinamalji siveric a nemang pasa kasasavan. 只要 他生氣就會把屋內的東西向 外扔出去。 
add: aicu a pinaka vavauan a dredretan papizuanan tua sinan paravac a zaljum ( vava ). 那稱為聖水之壺的陶壺是用來盛裝聖水(酒)。
add: aicu a vavauan a reretan inikamin a pinuvavan sikapalisilisiuta. 釀聖酒壺是用來裝酒和祭祀用。
add: ayatua iniyanan ka macaqu ti lanpaw a ljemangui ka ljemangui tjimadju se buqbuq. lanpaw 尚未學會游泳一下水就沉下水裡。 
add: na! manu namakuda sun a sika caucau! 唉喲！原來你是這 樣的人。
add: pinaka ti muni ni kina i eleng aku vuvu. 我的孫女被姨媽 eleng( 女子名)命名為muni( 女子名)。
add: aicu a sini vengetj tua qeluz a siravarava petjuq na zua ta lutlutan a siravarava. 用來綁柱子的這一 結繩子是剪自那一捆麻繩。
add: qadjavananga niamadju! 就任憑他們啦！
add: pailjaqa pusaladju! 請你ㄧ起幫忙吧！





Kanakanavu 
PROBLEM: the code and regular expression cannot discren the difference between Chinese half bracket ） and American half bracket ). So the code does not transcribe the pattern of  (\ \）.\s) = space + ） + . + space  (does not transcribe the Chinese half bracket) 

add: 祖父母的總稱或泛指已過世的長輩（百步蛇也稱tamu ）. manmaan ku parʉʉ'ʉna mataa tamu maku, 'ituumuru nguain tamna tavara'a. 我喜歡與爺爺聊天，他懂的很多。
add: 'ituumuru vatu matapari'i nesi, mastaan noo 'umo'ʉcanniin. 這裡有很多 落石，尤其下雨的時候。





Sakizaya 
PROBLEM: (the first one is because the definition ends with 。. and for some reason it is not being transcribed) 
add: tulu ku Banaw hananay ngangan nu niyazu'. 有三個部落名稱是叫Banaw。
(this sentence is being transcribed 2 times so I will also manually add it 2 times! ) 





Saisiyat
PROBLEM: the bracket is not closed, not fully transcribed   
delete: mal'az'aza' [ 在 賽夏族的生 命禮儀當中，從結婚到死亡共有五次的 回娘家儀式，分別是： 1. monSaySa:ip 結婚第三天回娘家
detele: So'o kita' ka hiza tata:a' balaS a hipo'? 你看看那隻雞是公的還是 母的？ [a 用來連接兩個成分，語言學上稱「連語」，出現的情況有以下幾個 1. 人名：子名 a 父名，如 'obay a kalih

PROBLEM: because of this pattern: …）. )  sentence not transcribed 
add: So'o 'amet ka hini tatimae'! 你吃完這些菜！ 
add: 'amet ka hini kasnaw! 喝完這碗 湯！
add: mal'az'aza' [ 在 賽夏族的生 命禮儀當中，從結婚到死亡共有五次的 回娘家儀式，分別是： 1. monSaySa:ip 結婚第三天回娘家 ]
add: So'o kita' ka hiza tata:a' balaS a hipo'? 你看看那隻雞是公的還是 母的？ [a 用來連接兩個成分，語言學上稱「連語」，出現的情況有以下幾個 1. 人名：子名 a 父名，如 'obay a kalih ]





Rukai
PROBLEM: for some reason, the regular expression: (\.{4}\s) is not catching any of the translation that has a definition ending in .... 
add: lri apaw lrimasu apavalavala liniane. 你要分五份給他們。
add: lu kaelaelasu lalakeisu madha capacape padrelreke. 你罵孩子時不要 打在背上。
add: mwakatwasa lalalrange. 走了，小心地走路。
add: luka kalaadravane ki acilay pangwaawsu madu tukange. 水漲的時候要 用網撈來捕魚。
add: kay tawpungu yai kapalrane madu lu mwinwane. 走任何地方狗是我 們真正的同伴。
add: ngwaladha kay tangwadrekanesu si kaseleme kai piapianga. 要為你這 次的跌倒 而不敢再做了。
add: tucaecape kay kamamadha. 木瓜的子較多。
add: this one is because it has a weird pattern: 1. 子多（如 南瓜、木瓜...）.  





yami 
PROBLEM: the ]/)is not fully transcribed, so need add ]/) to sentences 
add ] to: [以前，tao族一天只吃兩餐，早餐吃得早，所以到了下 午約
add ) to: ko ji akan o ya mizazaid a yakan. 我不敢吃有黏稠的菜。(如加了太白粉的 

PROBLEM: add sentences because their definition ends in ..... (5 American periods) / .... (4 American periods)/ ... (3 American periods)  and thus is not transcribed by the code
add: niomlapo no kalikey na, na katoda arakoan am, ya pa ji nimivias. 他從小到大，他 從未掃過地。
add: o amongan am, piyakanan so alibangbang. 飛魚盤是吃飛魚用的盤子。
add: koman ko so ikoa. 我要吃那個 ...。

PROBLEM:  add sentences because they are messed up by 3 american periods in the sentence before
add: ka pa ji absoy ori mo koaimo? 喂，你還沒有吃飽啊? ji ka ngai mo koaimo. 喂，你不要 跟來。 
add: asa doa tilo apat lima.... 一二三四五...。 

delete: 不直呼人名;不指明時間或物時之用語;如漢語的“那個…”之意. koman ko so ikoa. 
delete: asa doa tilo apat lima....





kavalan 
delete: 蓋棉被. 





Saaroa
PROBLEM:  …. (chinese ellipse + american period)
detete: 11 phrases after the ….  --> need to find them and detelet them. This list does NOT include them here. 

PROBLEM: because the definition ends in .... or .... (3 or 4 american periods), the sentence is not transcribed 
add: kuika kapitanʉnai hliangahli naani? 難道長官沒有來這裡？
add: ahlicita'ai ucani pihlingi mavahlaʉvaʉ mʉmʉa. 希望我們全家都平安。
add: kanakanavu nua ihlataia ucanika ahlamata. 卡那卡那 富族與我們亦出同源。 [未來式：ucaniaka]
add: kucikia pahlasʉkʉra paahlumʉlʉngʉsʉ. 咱們沒有辦法唱拉長音唱歌。
add: akuhlamu maini mana muasamu pʉtʉkʉhlʉ'a kʉmʉrangʉ tam saa'au. 以前我們 還是孩子的 時候，會捉kʉhlʉ'a 來燒吃，非常好吃。
add: pasakulaikiia puaruma amihlaina'anan pakiaturuana. 媽媽請老師趕 快進來。 
add: macikia kumita tavavusuia pasakulaikiia micuhlu. 看見眼鏡蛇要趕快走開。 
add: pasakulaikiia maini sikuatitipana. 請動作快 一點。
add: mavacangʉ a mi'a'aisa sala'ana ka, tumahla'ʉ cucu'u miacaacalivi. 他在 路上生意 很好，因為很多人一直經過。
add: kuakuarumuku 'amisana ta'iaraisaka kutuahlʉ musa patʉkʉ hluuhlungu pasaulaula'ʉ. 我不喜歡冬天，因為不能去溪邊玩水。
add: piavacavacangʉ iniciki maruka siaravacangʉ. 說好話才會 有好報。

PROBLEM: (because the definition has …….. / ……...(2 chinese ellipse + 2/3 american periods) --> if this is added to regular expression, it will undermine other patterns. Need to be added manually)  
add: piatʉkʉhlʉ vutukuhluia puatʉkʉhlʉ pangʉ'ʉ. 釣不同魚要用不同的 餌。
add: piavacavacangʉ iniciki maruka siaravacangʉ. 說好話才會 有好報。
add: ta'iaraisa ahlu'u naka tarapangʉ inicita maruka ʉpʉcʉahlu'u aanʉ. 因為蜜蜂 採花蜜，我們才 有蜂蜜可以吃。





Bunun
PROBLEM: add (I don't even know why this is not transcribed) 
add: Kavavaa maun haising! 快點吃飯！. [kavavaa ( 投高花東 )；ma-iskav ( 高)。]

PROBLEM: because the 4 。., the senetnces are not transcribed
add: Muntunuh tu daan hai, pahaisan; nii tu palahaib. 坍方 的路被劃界不可通行。
add: Masa dusang vali hai, pacinlaizu mas sinsusuaz. 從前有兩個太陽，使農作物枯萎。
add: Mais namacingaanin uvaaz hai, asa tu kadavus, na-istan-ali mavala. 當要為小孩命名的時候， 必須釀酒，用以招待姻親。

PROBLEM: the sentence is not fully transcribed because it ends in ？ .
add: Ciang, pasikuunsu sangan binaliv bunbuna? 江，你 剛才買的那些香蕉放在哪裡？
add: Mahansiap kasu maku-uni ahumushutcia ha? 你知道如何使 用那些套頸陷阱 嗎？

PROBLEM: the Chinese translation is not transcribed fully because the definition ends in ？.
add: Mabaliv aupa kata pang? 我們要買點麵包嗎？
add: Mavia sa-ia tu macishahainaz? 她為甚麼一 直跳著？
add: Namahtubin kamu padangian mas inaak tu pingaz-uvaaztan? 憑 什麼把我這個 女兒嫁給你們？
add: Andii sinhaili tu kanadaan hai, nii tu ma-aipi sistuh. 山刀的刀柄不容易?
add: Nalakua kasu kusia Takau? 你什麼時候 要前往高雄？
add: Maaz kazimaun suu maun? 你喜歡吃什麼？
add: Namaaz a isnavasu? 你要教什 麼？
add: Namaaz a tundaansu kusia Takaucia? 你要搭什麼去高雄？
add: Maazamaazang a duma haimangsuttan? 那些其他的東西是些 什麼？
add: Makinpia isuu isaincia kainludunan nasauzan mas utan? 你那邊有多少土堆要 種地瓜？
add: Makua isuu iniliskinan mas laupakadau tu sin-ihumis? 你對於現代生活的想法如何？
add: Namaazbin pakisaivunsu ii? 你到底想要什麼 啊？
add: Sima napasa- uni mas kakaunun? 誰要分配食物？
add: Adu mahtu taublasdanghas pinsial mata? 胡蘿蔔有益眼睛嗎？
add: Mashut aupa isuu sinlibatan? 你所栓的這個螺絲是否拴緊了？
add: Mavia utung tu mazima mavuhvuh lukistan ii? 為什麼猴子喜歡搖樹呢？

PROBLEM: need to delete 14 ? in total
delete: Mahansiap kasu maku-uni ahumushutcia ha? 你知道如何使 用那些套頸陷阱
delete: Ciang, pasikuunsu sangan binaliv bunbuna? 江，你
delete: Mabaliv aupa kata pang?
delete: Mavia sa-ia tu macishahainaz? 她為甚麼一
delete: Namahtubin kamu padangian mas inaak tu pingaz-uvaaztan? 憑 什麼把我這個
delete: Andii sinhaili tu kanadaan hai, nii tu ma-aipi sistuh.
delete: Nalakua kasu kusia Takau? 你什麼時候
delete: Namaaz a tundaansu kusia Takaucia?
delete: Maazamaazang a duma haimangsuttan? 那些其他的東西是些
delete: Makinpia isuu isaincia kainludunan nasauzan mas utan? 你那邊有多少土堆要
delete: Makua isuu iniliskinan mas laupakadau tu sin-ihumis?
delete: Napakisaivunta is-indangaz tu na-isnava
delete: Sima napasa- uni mas kakaunun?
delete: Adu mahtu taublasdanghas pinsial mata? 
delete: Mashut aupa isuu sinlibatan?
delete: Mavia utung tu mazima mavuhvuh lukistan ii?

PROBLEM: because of the 。., the sentences are not fully transcribed, need to delete (they are added fully above)
delete: Muntunuh tu daan hai, pahaisan; nii tu palahaib. 坍方
delete: Masa dusang vali hai, pacinlaizu mas sinsusuaz. 從前有兩個太陽，
delete: Mais namacingaanin uvaaz hai, asa tu kadavus, na-istan-ali mavala. 當要為小孩命名的時候， 必須釀酒，





Truku 
PROBLEM: needs to write a code to delete the pattern of this 
delete(this pattern):[相關詞-同義詞] + truku words 

PROBLEM: not being logged fully for some reason 
delete: [詞意：kari ini sneiyax 不信任 詞意： kari qlahang 小心 詞意： kari mqsiqa 含蓄語 詞意： kari kmrawah 婉惜 文化小語： 太魯閣族語有
delete: [詞意：kari tgearih 失望 詞意： mskluwi 驚嚇 詞意： ini snyax 不信任 詞意： mqaras 驚喜 文 化小語 ah在太魯閣族語是嘆詞，來表示狀 態或加強語氣， 以下說明ah的用語例句： 1.Ah! Ma su saw smdamat. 「啊呵！好久不見。」
delete: [相關詞-同義詞] uxay [ 詞意：ini tduwa 不可 詞意： ini sruwa 不答應（否定詞） 文化小語 花蓮的太魯閣族語通常會 使用aji，南投的德魯固語通常 用uxay 。 用aji形成的片語如下： 1.aj i uri o 「或是」 ；
delete: 1.lubuysnaluqraqilmiritpsaanbuji 箭袋；

PROBLEM: breaks in the middle of the brackets 
delete: Kingal ddmut ni

PROBLEM: because of some elipitcal pattern in the definition, the sentence is not fully transcribed
delete: Hhnu mu qmuyux ka bubung ga o iya ku haya ngali. 

PROBLEM: messed up by random/previous lines 
add: Eneinu ka saun su qmpah? 你要去哪些地方工作？
add: Hana su mowsa ka isu? Mdmdamat wada kana ka dhiya da. 他們都已經 走了，你才要出發嗎？

PROBLEM: because of some pattern, sentences are not fully transcribed// or sentences are in the brackets but are still useful sentences that should be transcribed 
add: Hhnu mu qmuyux ka bubung ga o iya ku haya ngali. 我用來......下雨的那個傘不要拿走。
add: Smlaa su bi sapah dxgal mu. 別在我土地上建房子。
add: Hnuyuq mu ka smbrangan o 50. 我磨尖過的矛有五十支。
add: Hnluluy mu ka dxgal o 3 tdruy. 我耙過的土已經三台車了。
add: A!qlungkumklada. 啊！我終於知道了。
add: A!ungathiyada. 啊！他死了。 
add: A!ajikuda. 啊！我不要了。
add: A!akaylnglung(laqi). 啊！我真的很懷念他（小孩）。
add: A!iyashaya. 啊！不要那樣。
add: A!hawansubinaqihnii. 啊！你這壞蛋。
add: A!Isunii! 啊！你這人喔！
add: ‘Aa!’ msa mnqhnga ni mskluwi. 「啊！啊！」這樣驚惶及驚嚇。
add: Ah! Ma su saw smdamat. 啊呵！好久不見。 
add: Ah! Ungat ki da. 啊呵！已經走了（死了）。 
add: Ah! Tayal su balay. 啊呵！你真是的。 
add: Ah! Rbangay su balay. 啊呵！你真要不得。 
add: Ah! Tayal su balay qnsjiqan. 啊呵！妳真漂亮。 
add: Ah! Ungat isu nii wa. 啊呵！你真沒用。
add: Snegeah na rmimu psbiyax ka laqi. 他以「啊呵」安慰鼓勵 小孩子。
add: Teeah mnkluwi kana. 都發出「ah! ah! 」的驚訝 聲。 
add: Ttghana dha mqqita o asi bi ptqrak mkkdamat wah! 他們才剛見面就互相思念 擁抱。
add: Asi khili hyaan ka isu da, pgealu bi ka risaw kiya! 你就嫁給他好了，那 男青年很可憐呢！

PROBLEM: there is english in the definition, which makes the whole sentence not logged 
add: Ma su kmnBowluk knan? Aji Bowluk ka yaku. 你為什麼把 我當作是 Bowluk ？我不是Bowluk 。





Thao
PROBLEM: ...... (6 American periods) ends some of the definition, making the sentences not transcribed 
add: tuqatuqashiza yaku! niwan! parhawaywan ihu! 我已經老了！還沒！你還年 輕呢！ 
add: thuini ya pulalu tamuqu, pisain tanalhiwan muqayiza putuan sa shupak. 今天拜tamuqu 時，只是把甜酒釀放在蒸桶而已。
add: mumu ya mahumhumiza sa qali amadunhuniza sa shanglaw a bangqir. 鼴鼠天黑後將會鑽損菜根。
add: afariwik thithu lhai suma, pakulhqaqlhak fariwik. 它要賣給別人，被我買回來。 
add: hau tu kahiwan inin'ianan Lai'azuan tuiza tu shashawin sa Lipun niza yamin tu isai Lay'azuan. 邵族人曾經住在Lai'azuan （今潭南）， 一直 到被日本人 驅趕，我們才不再住在Lay'azuan 。
add: haya inin'ianan thau mutaq. 有人在這裡 吐。
add: makuliushiza naak a bizu, akishkishakuan naak a bizu. 我的鬍鬚已經很長了，我要 刮一刮我的鬍鬚。 
add: thithu shmimul inisa naak a qlhup a tuali, min'iakin ukaiza sa inisa qlhup a tuali. 他借走我口袋裡的錢，使得我口袋裡都沒有錢了。
add: muqay miazithu. 只是這樣而已。 
add: muqay ihu miazithu? 你只是這樣而已嗎？ 
add: muqay miazithu a pashaila? antu maqitan riqazan! 戲只是這樣嗎？不好看！ 
add: muqay yaku a minlhalhuzu. 我抽藤要做魚笱。 
add: mihu a pazay ya antu pudanshiran uhu akaanin sa rumfaz alhthkiz sa rumfaz kmaan 你的稻子如果不做鳥 驚，會全部被鳥吃了。

PROBLEM: this bracket is cut half by the code. Even though we don't need the things in the brackets, this one has more sample sentences with translation. So I am adding them into the list 
delete: [●分辨： 1. 正確：numa s kalawan ihu iutu qa? 你在那裡做 什麼？
add: numa s kalawan ihu iutu qa? 你在那裡做 什麼？
add: numa s kmalawa iutu? 什麼東西 在那裡做 ？ 




Tsou
PROBLEM: for some reason, this sentence is not transcribed 
add: mitac'o ekameosʉ ho mita aomotʉ'ʉ 'e pasuya. pasuya 他只說得很簡短。