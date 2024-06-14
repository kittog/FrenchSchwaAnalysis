# Acoustic and Statistical Analysis of word-final Schwa in Parisian French: an explorative study
---

> **Note**: I am fully aware that in no way this is a complete project! However I've come to realise that perhaps I need to stop being overly perfectionnist, and rigorous when there's very little time, and also I'm already late so. In this concise report I'm presenting the outline I had in mind for this project which I failed to fully conduct due to multiple reasons.

## Introduction
### Context
The corpus used for this project is CFPP (Corpus du Français Parlé Parisien). Despite consisting of more than 80h of sociolinguistic interviews, all available as `.wav` files, the CFPP has yet to be fully exploited for studies driven by research questions on french's phonetic or phonological aspects. Many studies from Fleury, Lefeuvre and more focused on textometry, and the syntactic aspects of spontaneous speech: use of interrogative pronoun "quoi", *percontatives* are examples of such studies. The initial aim of my past summer internship (and this project) was to therefore conduct a pluridisciplinary study which would have linked Sociophonetics, Computational Phonology, and Natural Language Processing. \\

Ideally, the exploration of the CFPP would have led us to focus on fine acoustic details and retrieve acoustic and statistic insights that would provide a better sociophonetic understanding of the variations of chosen acoustic detail. This approach is mostly inspired by Jane Stuart Smith's work on glaswegian: through a sociophonetic lens, she documented sociological factors and phenomenons (social stratification of post-vocalic /r/, (Stuart-Smith, )) as well as the construction of locally-salient social identities (/t/ in Glasgow-pakistani highschool girls (Alam & Stuart-smith, )), linked to fine phonetic variation, in glaswegian. I believe that applying such methologies could be beneficial to our understanding of the french language and its variations. \\

In her recent works, Hansen studied parisian and suburban french on her own corpora, she focused mostly of nasal vowels and their evolution and confusion, as well as palatals and liquids. In 1979, Kikuchi studied the status of A-vowels (anterior a and posterior a) (Kikuchi, 1979). Hansen's earlier research however, focused on "e-prépausal" or pre-pausal schwa (Hansen, 1997 ; Hansen, 2003). More recently, Mathilde Hutin et al. (2021) explored the phonological of word-final schwa. As prepausal schwa is perceived as a indicator of social status (many attribute it to wealthier social classes -- speakers living in the western districts of Paris), I wondered if we could conduct a more in-depth study of final word schwa, whether they are pre-pausal or not: is word-final schwa (prepausal or non-prepausal) an indicator of social class? Can we map the variations around the productions of the phonemes and observe an actual split between western and eastern Paris (or Rive Gauche and Rive Droite ?)?  

### Speakers
As of now, it has not been stated by any of the researchers and volunteers working on this project that the corpora was complete: it is therefore regularly updated, with new transcriptions or even sociolinguistic interviews (the latest is from 2021). I selected 18 speakers from CFPP, some of which I had noted productions of prepausal schwa, by listening thoroughly to recordings. For each speaker, metadata is provided: age of speaker during recording, gender, job, studies, parents' socio-economic backgrounds, and Parisian district or suburban city which the speaker represented. \\

Although the CFPP presents various speakers, from different backgrounds, a large majority of them have pursued at least more than three years of higher education, and occupied well paid jobs (or jobs associated to a good social status). This is mostly due to how speakers were chosen: through the researchers' network (friends, family...). While prepausal schwa is associated to the Parisian accent, and especially to the wealthier social class, I was surprised to not notice more productions throughout the speakers. (Or perhaps for some speakers, it was harder for me to figure out whethere there were actual productions of prepausal schwa or simply nonchalant speech.) \\
Because prepausal schwa supposedly occurs more in spontaneous contexts, I've selected longer extracts from each interview, in which the speaker would speak continuously for at least 15s. \\

### Forced alignment and pre-processing
Forced alignement was performed for each audio file with its transcriptions through Webmaus MINNI, which output `.TextGrid` files with word and phoneme segmentation and transcripion, in SAMPA. \\
Before analysis and further annotations, all audio files were normalised.

### Data folder organisation
- `data`
	- `audio`: contains one folder per speaker. For each speaker, there are triplets of `.wav`, `.TextGrid` and `.txt` files.
		- `.TextGrid` files are Webmaus MINNI outputs.
	- `processed_audio`: normalised audio (as `.wav`) with the script `preprocess_audio.py`.
	- `results`: where the results of the analysis were meant to be stored (`.csv` etc)

## Methodology

> Most of the work was meant to be done in Python hence why almost all of my scripts were written in Python. However, because we also worked a lot in R in this course, I wanted to run the statistical analysis with R, using the functions and libraries we worked with throughout the semester.

### Schwa annotation
- `extract_phoneme.py` : wrongfully named, because it only aims to annotate schwas (whether they are prepausal or non prepausal). Ideally, the annotation of schwas would have been more accurate if I had managed to write a script to detect the prepausal schwas (with their nasalisation). In this script, I annotate a schwa as pre-pausal if the next interval was labeled by Webmaus as a pause (`<p:>`) which is reductive. Annotations are then saved as TextGrids but the script is not fully working, and I struggle to make do with the textgridtools documentation and API. 

### Acoustic analysis
- `acoustic_analysis.py`: once schwas are all annotated, we can then extract acoustic measurements. In this script, it is with `parselmouth`.
- `opensmile_measures.py`: I made this script last summer and eventually optimised it back in January. Extracts measures from `.wav` files (from given folder) with the openSMILE Python module.

Technically, I wanted to run the acoustic analysis with the measurements taken with `parselmouth`, and then run the statistical analysis with the openSMILE measures.

For the acoustic analysis: get formants, intensity, and _pitch_, which I believe is an important factor to consider, especially with prepausal schwa as pitch gets higher, and the schwa itself can tend towards a nasal vowel. It would have been interesting here to compare acoustic features for prepausal and non-prepausal schwa: ideally, the acoustic analysis would have helped us determine which acoustic fine details were significant in the differentiation of prepausal and non-prepausal schwa.

### Statistical analysis
Using the openSMILE measures: I believed that running a cluster analysis with k-mean clustering would help us visualise whether or not we can cluster productions of schwas among speakers and if we can, what would the clusters tell us about the speakers studied.
In this script, I've only run the k-mean clustering algorithm, but to figure out how many clusters we could possibly have within our data, it's recommended to perform hierarchical clustering first. The output of the latter will help us determine k. \\

By exploiting the metadata provided by the CFPP, we could have perhaps observed if the obtained clusters represented certain areas of the parisian region, gender, or socio-economic status. \\ 

Because each sociolinguistic interview is thorough and goes over the speaker's personal life and experiences, we can easily complete our analyses with sociological informations provided by the recordings, as well as the metadata.

## References
- Anita Berit Hansen, Les changements actuels de voyelles nasales du français parisien : confusion ou changement en chaîne ? (2001)
- Anita Berit Hansen, Le e-prépausal et l'intéraction (2003)
- Anita Berit Hansen, Le nouveau e-prépausal dans le français parlé à Paris (1997)
- Jane Stuart-Smith, Social stratification of post-vocalic /r/ in Glaswegian adolescents
- Farhana Alam, Jane Stuart-Smith, Identity and ethnicity in /t/ in Glasgow-pakistani highschool girls (2011)
- Louise Kikuchi, Status of A-vowels, The French Review (1979)
- Hutin et. al, A corpus-based study of the distribution of word-final schwa in Standard French and what it teaches us about its phonological status (2021)

