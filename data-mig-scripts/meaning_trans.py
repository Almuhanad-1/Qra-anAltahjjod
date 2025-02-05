import json


def text_to_js_array(text):
    lines = text.strip().split("\n")

    objects = []
    for i in range(0, len(lines), 2):
        range_str = lines[i]
        description = lines[i + 1]
        range_parts = range_str.split("-")
        if len(range_parts) == 1:
            range_start = int(range_parts[0])
            range_end = range_start
        else:
            range_start = int(range_parts[0])
            range_end = int(range_parts[1])

        obj = {"range": (range_start, range_end), "description": description}
        objects.append(obj)

    js_array = (
        "["
        + ",\n".join(
            [
                f"{{range: [{obj['range'][0]}, {obj['range'][1]}], description: '{obj['description']}'}}"
                for obj in objects
            ]
        )
        + "]"
    )
    return js_array


sample_text = """
1-2
وظيفة القرآن الكريم، والقرآن كتابُ هداية وإرشاد.
3-5
بيان صفات المتقين، وأن الإيمان بالغيب هو من أهم صفاتهم.
6-7
بيان صفات الكافرين، وحقيقة الكفر، والكافر هو الذي يُبادر ربَّه القطيعة.
8-16
بيان صفات المنافقين وجزاؤهم، وقلب المنافق مسكن للكفر.
17-20
ضرب الأمثال في المنافقين وبيان لحالهم وضلالهم.
21-22
خطابٌ لكفار مكة وللبشرية بالحجة والبرهان، لأن الإسلام دين حجة وبرهان.
23-24
الإعجاز والبيان القرآني حجة لله على خلقه، وبيان لجزاء الكافرين.
25
تبشير المؤمنين بالجنة وبحسن جزائهم في الآخرة.
26-27
الاستدلال على الحق بكل مَثَل وبكل كلمة لا مانع من ذلك.
28-29
ميثاقُ الله على خلقه بعدم الشرك مقترنٌ بكل خير، وبيان لقدرته تعالى في الخلق والبعث.
30-33
قصة بداية خلق البشرية، واللغة علمٌ وإلهامٌ رباني وليست بدعة بشرية.
34-39
استكبار إبليس عن السجود لآدم، وتكرُّمُ الله تعالى على خلقه بقَبُول التوبة.
40-48
دعوةٌ ربانية لليهود، وذكر للعهد الذي أخذه الله تعالى على بني إسرائيل باتباع النبيِّ محمدﷺ.
49-52
بيان لكفر بني إسرائيل بنعم الله الكثيرة التي لم يقابلها التوحيد بل قابلها عبادة العجل وعندما تابوا تاب اله عليهم.
53-57
طبيعة بني إسرائيل المادية لم تؤهلهم للاستمرار بمعرفة الله عز وجل ومراقبته فعبدوا العجل.
58-59
كشف لحال بني إسرائيل وخبثهم، وإنَّ الحماقة في الاعتراض على الحق جل وعلا، وعين الكفر الاقتراح عليه، والمعصيةُ بابٌ للذل والمهانة.
60-62
طلب الرتبة الدنيا بين العباد من خشية الله سبب للذل في بني إسرائيل،وطلبهم مآكلاً دون ما أعطاهم اللهعز وجل سبب لمسخ فطرتهم إلى يوم القيامة.الصلةُ بين الحق والخلق، وإنَّ من شروط دخول الجنة الإيمان بالله وباليوم الآخر.
63-66
تذكيرٌ بالنعم الربانية، إنَّ الذين لا يؤمنون بالله تعالى ومواثيقه يعرضون أنفسهم لكل عقاب.
67-73
قصة بقرة بني إسرائيل، ومجادلة اليهود وعنادهم وكشف لطبائعهم.
74-75
بعضٌ من صفات بني إسرائيل، إنَّ دين الله يسيرٌ ولن يشددَ الله على العباد إلا بمعاصيهم، والإعراض عن الله تعالى سببٌ في قسوة القلب وغلظة الطباع.
76-77
النفاق والتقية بالباطل طبع من طبائع الشخصية اليهودية.
78-79
بيان لتحريف التوراة، وتحريف كتب الله تعالى له عدة أشكال ومنه التفسير الباطل.
80-82
دخول الجنة باتباع الشرع، ومقاصد كتب الله متماثلةٌ في التوحيد والدعوة إلى الخير.
83-86
ذكر لمخالفة اليهود عَهْدَ الله تعالى ونقضهم للمواثيق واستحقاقهم لغضب الله.
87-88
التحريف العملي للتوراة عند اليهود وذلك بالالتفاف الخفي والمخالفة الصريحة.
89-90
تكبر اليهود وكفرهم بمحمد ﷺ، ومعرفة اليهود للقرآن كانت يقيناً.
91-93
أكاذيب اليهود وقتلهم لأنبياءهم.
94-96
حبُّ اليهود حياتهم الدنيا وحرصهم عليها، والدنيا سجنٌ للمؤمن وجنةٌ للكافر.
97-98
عداوة اليهود للملائكة والرسل عداوة الباطل للحق، وإنَّ الذين يعادون أولياء الله قد آذنهم الله بحربه.
99-101
بيان لعدم وفاء اليهود بالعهود، وبشارةٌ بمحمد ﷺ.
102-103
عصمة سليمان عليه الصلاة والسلام مما نسب إليه.
104-105
استقامة الأمة الإسلامية، وكشف مكائد اليهود، ومن طبيعة الكافر حب الشر للآخرين.
106-108
النسخ في القرآن، والله المتصرف بما يريد، يتصرف بملكه بما يشاء، والرد على اليهود.
109-110
حقيقة أهل الكتاب وخبث نفوسهم، والاعتراض على الله نهايته الكفر ثم عذاب جهنم.
111-112
افتراءات اليهود والنصارى وأمانيهم، ودخول الجنة بالإيمان والعمل الصالح.
113
دعوى بلا دليل، والدعوى بلا دليل ظلمٌ يعود أذاه على صاحبها.
114-115
حرمة المساجد، وعبادة الله تعالى أمانٌ للبشر، والذي ينشر الخوف يصاب به.
116-119
افتراءات المشركين على الله، ومنهج الكفار في الإعراض عن الله سبحانه.
120-121
تحذير من اتباع اليهود والنصارى، والتعصب الأعمى ليس دليلاً على الحق.
122-123
بيان فضل الله على بني إسرائيل، وتذكير بخصوصية الحساب يوم الدين.
124-129
مقام إبراهيم عليه السلام أبو الأنبياء، والبيت الحرام قبلة العبادة لأهل الأرض جميعاً، وبناء إبراهيم عليه السلام للكعبة المشرفة ودعاؤه عندها.
130-134
التأكيد على اتباع ملة إبراهيم عليه السلام وهي الاسلام والتوبيخ لمن ابتعد عنها.
135-138
بطلان دعوى اليهود والنصارى باتباع ملتهم، وبيان بأن الإسلام هو الدين الحق.
139-141
رد على اليهود والنصارى، والحق هو في طاعة الله واتباعه واتباع رسله.
142-145
مناقشة قضية تحويل القبلة، والتألي على الله فيما لا علم لنا به نوعٌ من السفاهة وقلة الحكمة، وإن البيت الحرام مذكور بالعظمة في الكتب السابقة.
146-150
كتمان أهل الكتاب للحق، ومخالفتهم للرسول ﷺ.
151-153
منةٌ من الله على المؤمنين ببعثة النبي محمد ﷺ، وقراءةُ القرآن تكفي للتزكية في هذه الأمة.
154-157
بشاراتٌ ربانية للمؤمنين، والإيمان بالله يعين على الصبر، والإيمان بالقدر من أركان الإيمان.
158
الحج عبادة لله، والعبادة وهيئتُها تشريع من الله تعالى وهو الذي يقبلها أو يردُّها.
159-162
بيان لفضيلة نشر العلم وعدم كتمانه، واللعنة والجحيم من الله على من يشرك به.
163-164
حبُ الله تعالى ودوافعه الكونية.
165-167
سوء عاقبة المشركين بعبادتهم غير الله، وكل من اتبع أحداً دون الله سيتبرأ منه يوم القيامة.
168-169
من نعم الله تعالى على جميع الخلق، وأهل الباطل أهل بغضاء وعداوة.
170-171
عدم اتباع المشركين للإسلام، والحق لا يُعرف بالأشخاص.
172-173
التحريم خاص والإباحة عامة وآيات من الله في تحريم أطعمة ذات ضرر.
174-176
كتمان الحق نوع من الكبر يبوء صاحبه بغضب الله وعقابه.
177
مبدأ البر، والتقوى والبر هي معانٍ وأعمال وليست صورٌ وأشكال.
178-179
القِصَاص وتشريعه والحكمة منه، والقصاص هو سبب لحماية الحياة الإنسانية.
180-182
تشريع الوصية والميراث، والأقربون هم أولى الناس بقريبهم فيما تركه من ميراث.
183-186
تشريعات ربانية في الصيام وبيان لأحكامه، والصيام عبادة في شرائع الله جميعاً.
187
تشريعات ربانية في الصيام، ورحمة الله لهذه الأمة أساس التشريع الرباني الأخير.
188
تعظيم حرمة مال المسلم، والذي يأكل المال الحرام هو الأدنى.
189
أجوبة في الحج، والأهلَّة هي مواقيت للعبادة.
190-194
تشريعات في القتال، ثم تشريعات جهادية لحماية الدين الحق في حال أي خطر متوقع عليه، والمعاملة بالمثل حق ولا ينبغي الزيادة عليه إلا بإحسان.
195
الصدقة في التشريع الإسلامي، والإنفاق في سبيل الله صنو الشهادة والقتال وهما ثمن الجنة.
196-203
تشريعات في الحج والعمرة، الإحصار وحج التمتع ورخص الحج، وأيام التشريق وذكر الله فيها كثيراً، مؤتمر الحج برهانٌ على سمو هذه الأمة.
204-207
مثل الصلاح والفساد، وإن الله لا ينظر إلى صور عباده بل إلى صدورهم وقلوبهم.
208-210
دعوة إلى المؤمنين للدخول في طاعة الله، وتحذير من معصية الله.
211-212
تذكيرٌ ببني إسرائيل، والمثل ينفع للعظة والعبرة.
213-214
إرسال الرسل إلى البشر، وحاجة البشر إليهم، وصبر الرسل وأتباعهم على الأذى.
215
أحكام النفقة وبيان المستحقين لها، والنفقة هي من أصناف الابتلاء وسببٌ في النصر.
216-218
مشروعية القتال وأحكامه.
219
أحكام في الخمر والميسر، ومحو السيء والاتصاف بالخير.
220-221
تكافل المجتمع المسلم، والتربية النفسية في الإسلام تنشأ من الداخل، والولاء في المجتمع المسلم (لله تعالى وحده ولمن آمن به) وأحكام في الزواج من المشركين.
222-223
أحكام الحيض، والطهارة في الحياة الأسرية شاملة حساً ومعنى.
224-225
أحكام اليمين وتعظيم الله تعالى.
226-227
بيان أحكام الإيلاء.
228-230
تشريعات في الطلاق وتبعاته وتماسك المجتمع المسلم هدفٌ من أهداف التعليمات القرآنية.
231-232
معاملة المطلقات، وتدل الآيات على أن مراقبة الله تعالى هي التي تسير المسلم في السر والعلن.
233
أحكام في الرضاعة والنفقة.
234-237
في ثبوت عدة المتوفى عنها زوجها، والحفاظ على الأسرة والوفاء للزوج شيء ثمين في شرع الله، والاستقلال المادي للمرأة هو من إكرام الإسلام للمرأة، ووجوب نصف المهر قبل الدخول.
238-239
من أحكام الصلاة وآدابها، والحفاظ على الصلوات له أثر عظيم في الحياة الفردية والاجتماعية، والحفاظ على الصلوات مطلوب مدى استقرار الروح في الجسد.
240-242
تشريعات في الطلاق، عدة المتوفي عنها زوجها ومتعة المطلَّقة.
243-245
بيان جهادي من زمن بني إسرائيل، والإنفاق من المال صنو الجهاد في سبيل الله.
246
العبرة من بني إسرائيل في كل شيء من خصائص سورة البقرة لهذه الأمة المسلمة.
247-248
جعل الله طالوت ملكاً على بني إسرائيل ليجاهدوا في سبيل الله، ومجادلة بني إسرائيل فيه.
249-252
متابعة البيان الجهادي واختبار الله تعالى لجنود طالوت بالنهر وانتصار الفئة القليلة وقتل داود عليه السلام لجالوت، والصبر هو من عوامل النصر الأولى.
253-254
الهداية بالرسل والرسالات، والاختلاف من طبائع النفوس البشرية، ودعوة للإنفاق في سبيل الله.
255
آية الكرسي، والعقيدة الإسلامية وأثارها، والإيمان بالله تعالى أعظم غاية في الوجود.
256
الدخول في الاسلام يتم عن طريق الإرادة والتفكير لا عن طريق الإجبار.
257
المؤمنون يتولاهم الله والكافرون أولياء الشيطان.
258
مجادلة النمرود لإبراهيم عليه السلام، وأمثلة على قدرة الله تعالى.
259
قصة الذي مر على القرية، والطاعة لله لا حد لها والمعصية والكفر ظلماتٌ تفضي إلى النار.
260
إبراهيم عليه السلام وقدرة الله في إحياء الموتى.
261-264
أهمية الإنفاق في سبيل الله، والإنفاق في سبيل الله أجره عظيم لا يعلمه إلا الله.
265-266
الإنفاق في سبيل الله يعود خيره على المجتمع كله وينفع الإنسان في ذريته.
267-269
الإنفاق في سبيل الله لا يقبل إلا إذا كان حلالاً طيباً ويجب إخفاؤه عن الناس.
270-271
صدقة السر خير من صدقة العلانية، والله لا يخفى عليه شيء.
272-274
الهداية من الله، ومن الحكمة في الصدقة أن تبحث عن أصحاب الحاجة الحقيقية، والصدقة قوة في الروح والنفس والجسد.
275-276
تشريعات في تحريم الربا، أكل الربا إثم عظيم ومرض روحي وعقلي على من يتعاطاه، والربا نهايته الخراب والدمار لعلة الشح والظلم.
277-281
تنبيه المؤمن إلى العمل الصالح والابتعاد عن المكاسب الخبيثة.
282-283
أحكام الدَّيْن، وتشريع في مصالح العباد ورعاية حقوقهم، والإشهاد على الدَّيْن سنة ربانية، والنسيان من طبع الإنسان، والضرر ليس من شرع الله بل هو فسوق وانحراف.
284-286
الرحمة في الحساب الرباني، والإيمان بالله رأس أركان الإيمان، ومن رحمة الله وكرمه أَنْ حط عنا ماليس بمقدورنا وجعلنا نلتجئ إليه دوماً.
"""

js_array = text_to_js_array(sample_text)
print(js_array)

# Specify the file path to save the JSON data
file_path = "./1-meaning.js"

# Write the JSON data to the file
with open(file_path, "w", encoding="utf-8") as js_file:
    json.dump(js_array, js_file, ensure_ascii=False, indent=2)
