def find_similarity(puzzle_input):
    similarity = 0
    puzzle_list_1 = []
    puzzle_list_2 = []

    puzzle_splitlines = puzzle_input.splitlines()

    for puzzle in puzzle_splitlines:
        if puzzle.strip():
            puzzle_1, puzzle_2 = map(int, puzzle.split())

            puzzle_list_1.append(puzzle_1)
            puzzle_list_2.append(puzzle_2)

    for puzzle1 in puzzle_list_1:      
        number_of_puzzle = puzzle_list_2.count(puzzle1)

        similarity += puzzle1 * number_of_puzzle
        
    return similarity

def main():
    puzzleInput = """58990   83989
26183   15707
48195   12659
20176   26012
26730   42699
85161   27706
96982   95631
87996   58243
39657   41171
78872   33231
34487   72728
29811   99268
21721   49694
26489   66506
42015   20464
27364   97109
74634   96288
97761   76904
55760   27706
73395   44236
70292   87279
23732   31037
35979   98965
39607   13469
47127   79924
92247   33911
46961   33231
91221   31037
78652   83821
37026   62907
11525   26730
44193   92319
25735   33249
69120   32589
48384   46622
31056   71217
21738   33911
58732   61515
24566   33911
44699   25959
14669   87970
67130   25959
43796   87726
23106   54813
96034   67811
35340   98556
71868   97692
33492   54616
51373   35614
99072   95208
39427   64273
92427   33911
33558   69302
89049   99150
43382   71632
48018   99449
11476   67811
61065   23675
40706   55203
38289   20464
61388   19960
10173   78890
73579   32327
79707   92137
28812   42327
86825   57070
20684   31037
51239   99150
81140   34779
76168   99150
99264   47093
26913   35996
94683   88397
78541   49558
67469   89113
21163   77443
17512   58592
98081   14460
59759   33911
14953   98556
44472   52439
95878   10311
45177   71299
94802   33231
78885   54616
32894   56495
81586   73037
20780   21728
45722   83302
57179   33911
58010   13033
18803   12885
31369   67973
47417   75886
23725   90560
24171   41980
41159   98556
86721   46022
42213   89733
67094   90269
42824   60452
75980   31037
57308   76611
71184   40177
92274   89725
17355   76918
21401   88969
41141   82206
26962   22168
58595   17840
74713   75610
64974   30283
81081   41393
65538   32330
79576   67054
45311   42563
53579   97692
27706   43952
33000   88917
94880   68771
58409   63351
62237   79967
95180   25790
75624   80977
87121   86053
20214   72368
37248   31153
81130   50096
93290   74779
48621   44148
55488   11750
30294   25790
18426   34334
61159   37275
66015   58595
22543   81784
22836   49558
75789   36896
89780   88896
80626   54609
79138   49500
32331   51373
64732   94408
64384   25959
98590   16398
32268   66516
76414   88397
14193   13469
59330   26730
34093   10311
83585   75324
95643   51373
61401   64620
38442   55909
93684   80680
26110   34957
15441   24332
92433   49558
28327   55141
21955   13469
49694   10893
25544   94388
84691   58243
79194   94680
16801   65278
49387   17840
26366   63022
98455   41105
80499   33231
68980   67811
93089   80086
90633   98556
48942   32327
52095   88397
35173   20464
50528   15228
48435   25959
78990   31641
57862   52439
83194   32327
11974   71373
55908   46627
67541   42458
44245   54654
20222   52439
35725   33787
23053   49558
67114   49561
39907   62721
26882   90072
83894   88397
48151   89230
45532   20122
54616   43083
29225   87279
23310   49694
27391   89779
81010   80680
37854   31037
12301   81934
60653   62188
39146   24897
19921   83997
20491   86255
20704   98554
89603   24418
48990   98965
17859   59190
91770   20464
26894   51373
71700   26730
53034   52439
64173   50150
35643   82272
47856   49558
41758   99150
25314   29584
89505   83762
33384   59580
90660   95080
36669   26730
77226   25562
22259   73630
30997   20464
49539   66511
61452   22708
44075   79857
53649   25790
60788   58595
47920   32327
19137   73043
41111   44410
68368   17840
13793   30684
60368   27410
26012   34148
51252   57009
43496   97692
65956   13469
18306   84529
84742   26730
10586   56357
69115   37394
30697   82636
73975   52439
98556   22168
72653   28561
92806   52439
70605   39685
79072   11939
28964   63109
64155   25959
33721   10311
72727   59988
42141   22708
38511   33231
73842   98965
39787   10956
67974   32926
39281   13469
78547   17840
86630   80730
65830   71632
30096   52439
83498   88397
79839   68049
36667   58595
34592   15526
55976   71632
29750   97528
83649   38418
49774   16314
45369   58595
25790   73805
28234   13874
64287   31037
14200   82623
67555   25790
23415   25790
51011   58243
35467   26012
88385   33922
64333   98965
93289   14155
78046   53761
61252   72609
56317   86600
39616   83714
40974   48045
89183   44236
71298   20464
40425   98556
44622   40331
16769   32327
50032   13469
94307   21621
67797   87043
53067   98965
44986   78348
97030   79597
16328   89331
28732   99527
14888   80769
76256   25959
12080   31216
20532   87498
65920   79221
82906   13469
68188   71544
35079   32327
40756   52439
96432   22198
24716   25959
97265   27706
40357   57909
78488   39786
58117   30532
53542   74875
80762   56553
73211   97463
34760   22294
72386   51373
24765   83968
77969   97636
42632   64391
73252   16844
43182   82974
22905   42642
71363   52439
18432   51474
80171   58243
80504   72049
87491   22168
94636   19806
90824   43498
76821   41878
97208   58243
39385   18510
25328   35469
47426   49558
41105   51373
86595   25959
25289   20464
14654   75836
98168   33802
52229   15427
77059   80312
33191   20464
56474   81018
84198   98491
30272   85675
95046   27870
46439   80680
42491   80680
17801   41607
25959   96386
14098   52439
67001   40744
53899   49888
35932   88615
60024   98965
51738   52439
44766   17840
99310   48015
57320   75523
91218   13940
79971   84186
61698   19307
15416   49558
60942   40468
33231   33231
82304   37067
13091   99150
34120   71471
62522   81211
51195   90298
86959   58595
13469   96220
26437   51351
17377   58243
20482   34401
58540   33911
44464   31037
76660   28713
65570   33231
68702   29170
13732   48144
37635   10311
40758   91054
88294   20464
57997   98780
15322   88397
15026   27870
10311   25959
40709   35778
49931   45153
78146   99353
35434   88397
21586   55141
14306   41466
54907   82131
39348   33911
34528   48569
85498   27870
97692   50901
93336   31037
93579   99784
70893   20464
98547   99150
99653   71632
97792   52439
94428   91785
47952   28237
46700   42531
82623   87524
51986   22708
95299   82459
90152   88865
21647   21625
51079   90706
76530   99864
16685   12061
15557   69728
27693   98965
30323   30876
33846   25959
36900   28621
51501   88397
79980   45861
96871   26012
94536   54616
13619   32327
12633   54616
29434   99150
37371   12715
30592   19467
61834   98965
37159   11465
76104   73667
42439   93792
12737   71632
40599   97728
78945   45461
26422   87279
40048   25790
33252   25199
64705   33231
38425   50988
34650   89998
77866   99150
42426   97850
86881   97692
31037   49027
24284   52439
31351   26600
11314   63580
40512   99150
61317   51373
86804   27200
93217   84636
54264   20464
71848   25105
41317   17840
20822   94183
13434   32327
75294   63872
45871   88397
94496   28919
79486   31037
73469   51920
73321   25790
84632   88397
13797   25790
81243   51373
49923   90162
17133   90672
70647   42099
77767   13062
11890   97692
99150   46800
22576   53468
57589   25361
19897   26730
17826   21976
81918   72722
10494   59416
95897   10311
25338   85339
55840   24358
47904   32327
64695   55141
97909   41087
49800   17199
23393   45735
44112   40395
34177   58243
45093   88397
13531   27870
11685   17840
61846   49694
19864   41105
71711   14196
41935   55742
30456   73366
93167   37656
54262   26012
16943   73066
56485   31037
83422   99150
27202   49558
32209   98973
18566   98556
71881   20464
90696   49901
83872   97692
33911   89520
79411   10982
39840   55119
18184   49558
72608   59553
75060   19448
99717   26008
27870   99150
79388   55141
88792   74946
87743   44236
21381   22708
16604   26012
79422   22708
99518   17840
43538   20464
59793   49694
51360   32327
71095   18697
54403   13469
87694   27870
99606   38781
56481   27637
52566   87874
85672   17840
10619   33231
49467   58243
74518   54616
84128   46916
21960   73325
20817   81944
41972   10311
41531   28597
52167   69556
33057   49558
20059   61122
58246   49558
96285   31037
58243   12449
20464   21688
43638   51863
61636   26012
95169   17442
39758   27540
81693   58564
67992   35284
87449   57059
26498   56170
70154   32327
39639   94226
43560   98965
71691   58595
97372   27040
86291   58243
93329   87286
37007   90197
50905   43748
95718   33036
53073   94048
95566   88397
37931   45535
44437   25959
69216   85393
68537   33911
89154   58243
83662   58607
96102   78378
93495   30297
37697   78352
51030   73399
43139   17315
89941   80561
74566   42345
71613   33715
53213   19951
35094   25866
25142   23986
97531   20824
36336   97692
56464   17840
98880   25959
40170   15790
68370   32327
62746   91777
14815   47770
82609   53322
37384   26572
79298   10311
15994   85092
24667   88397
62232   20464
76536   75320
22168   97692
47532   99882
83915   25790
53594   98556
44185   25959
33847   81474
80172   58243
92387   51155
77286   27870
58407   20464
51798   31037
85681   40873
98604   33911
23193   10311
42207   24730
29275   44653
38883   73550
64149   32327
94968   88747
88949   75785
23467   81864
24672   60634
31844   22708
63168   20464
18630   67458
25936   32327
99788   65630
76153   47192
64820   88894
48127   41006
42549   39491
36028   94108
65511   36428
83631   17527
30705   68759
63816   41105
49162   76956
64635   54824
35428   37327
85354   58595
43910   31289
34988   68656
59695   71632
56126   19390
79593   32327
60787   99150
65297   54606
71667   51373
78750   35414
28176   35321
30235   26012
29589   26012
94484   22708
28976   33911
10891   39188
82415   26012
17840   88397
12362   82623
44689   56497
32329   17840
36224   98556
49558   12520
36420   21364
24294   36318
55624   90378
40840   93019
51198   31037
87483   21075
93982   79772
50567   87279
61386   59761
65062   79864
20280   82100
19901   71632
75786   46099
79105   27870
52900   44803
15376   98556
24811   44210
75536   74306
49782   57620
61537   32130
75088   75904
60963   85542
65756   51725
77859   96787
34133   17840
99910   70330
98965   33911
65548   92432
85173   32752
97683   70578
74299   88397
58858   69589
80192   88397
34718   27870
16716   31037
70433   47321
47024   48665
30642   87279
94495   97692
87606   33911
18984   33911
44236   93040
91312   44915
91687   59401
54787   14448
55489   58254
55141   65394
27106   45500
68857   69327
85898   62022
94901   80680
50502   98965
98505   19302
30563   31037
66131   88397
20133   70635
83377   38650
33954   91671
97110   46037
14452   32533
17300   82532
18761   47202
74745   95535
91644   40500
28553   87279
94128   71899
33420   33797
92910   99150
37708   72908
61526   20464
76908   74639
10971   18271
63791   72651
99823   23737
36476   84997
47467   91743
86834   67811
67811   10311
66608   21028
57189   10311
90548   35661
27994   94117
41778   84101
81713   90550
29172   36583
97018   56756
16240   79873
40946   99150
12112   79991
11426   64939
84378   87279
82230   65726
80395   58243
12832   52917
81595   81384
46567   83604
73987   85489
29682   17840
26890   52439
60282   13469
29069   98965
51151   24098
23646   58828
97787   26012
25233   96638
22366   97982
18027   74245
74870   33231
65024   44767
95515   91430
27288   64938
53260   93877
47304   80434
79764   77500
13760   36198
52147   13732
97016   26984
72787   15983
82709   78450
79236   71632
67107   25959
51400   29710
68826   97692
58799   42756
81849   29891
50383   49043
35715   70394
36380   71632
74160   78588
22634   33231
80680   25959
55881   33911
67404   48000
40509   49558
71229   44236
74570   13469
32180   71632
17190   76323
20574   99580
39284   89698
87279   36191
52715   17142
23554   10392
32327   31339
69747   30887
62207   88397
83704   81078
75085   18344
29775   18477
60519   27870
43842   23095
40417   62592
36659   48017
15188   29519
79365   93885
18236   72179
44401   97966
28839   80680
70555   13469
16791   31892
85629   51728
74917   52509
56386   69664
70126   73109
71807   20464
21971   58243
23752   94017
45368   88397
29547   27283
35796   66651
56091   51373
85503   28778
40279   22708
62551   55346
25734   14804
95005   95049
51899   63155
22708   46060
41722   95729
71824   37142
59191   99274
82083   25959
78078   99150
15421   56253
31581   61593
76784   44236
65374   89414
45587   86495
64550   82113
97345   69762
36835   31480
15341   31037
45365   82638
61872   61538
64106   49345
64928   98413
47863   49558
27558   33911
82444   27063
74039   17644
53966   32390
21022   67811
49180   98950
52439   32327
86696   57405
25627   95357
29897   97963
29661   32327
98440   15331
20550   37870
49301   54616
67774   13469
19807   29401
91869   31037
74742   42872
30790   17840
29664   23132
55595   46418
25650   97692
81699   25959
88579   53267
85213   47433
50079   90511
38163   28443
11279   41105
66102   52439
73407   68587
16501   57839
97144   62521
28719   26237
48422   38113
27017   10311
30367   93821
58740   37160
82350   95594
19614   41334
75354   26730
14743   97692
71164   91177
40824   12317
29278   97692
78783   95869
15291   88541
99134   35793
51179   14442
61656   12198
36903   33231
42998   18567
32769   71632
38966   85081
61111   42408
43774   39223
83954   67811
62774   28337
23009   54616
83587   29814
11625   81703
85067   98556
79235   62042
27666   52439
71757   22168
63856   50515
74642   98013
84731   34159
82822   49694
98821   87023
18490   70325
31172   33231
50837   58243
16889   12338
47909   29925
27911   75634
92573   97692
99821   27870
16051   68857
90386   58243
15508   97537
94585   54482
42254   16585
88061   98650
48365   27870
48985   97692
68310   22168
51604   10181
37019   14118
25177   12130
12805   48734
44481   95568
66499   56369
58999   87279
81515   18858
13380   25790
92225   60825
85816   18987
66727   13241
12136   35829
41350   87296
76507   56008
14899   50028
70570   44236
87699   88397
86079   30962
75223   32327
86547   68650
39093   98984
49677   54616
62894   33231
71584   32003
63695   86633
20393   77961
61359   82477
80230   39901
35130   80105
29488   88473
31018   99892
71632   33911
21296   22499
46649   67665
40806   83947
85856   25790
17380   10311
21611   54616
88397   67286
84967   32327
75283   13469
86602   71632
97062   69801
74487   38552
98205   31037
52941   64568
16747   22277"""
    print(find_similarity(puzzleInput))
    
if __name__ == "__main__":
    main()

        