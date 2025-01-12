import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from streamlit_carousel import carousel
from PIL import Image

# Images
trophy = Image.open("./Images/Trophy.png")
silverstone0 = Image.open("./Images/Silverstone_Start.png")
silverstone1 = Image.open("./Images/Silverstone_Final_Turn.png")
silverstone2 = Image.open("./Images/Silverstone_PK_Zane.png")
australia_circuit = Image.open("./Images/Australia_Circuit.png")
australia1 = Image.open("./Images/Australia_Start.png")
australia2 = Image.open("./Images/Australia_Collage.png")
australia3 = Image.open("./Images/Australia_Side_Shot.png")
spa_circuit = Image.open("./Images/Spa_Circuit.png")
spa_collage = Image.open("./Images/Spa_Race_Week_Collage2.png")
postponed = Image.open("./Images/Postponed.png")
spain_circuit = Image.open("./Images/Spain_Circuit.png")
spain_cover = Image.open("./Images/Spain_Cover.png")
spain_yeti = Image.open("./Images/Spain_Yeti.png")
spa_nick_joshua = Image.open("./Images/Spa_Nick_Joshua.png")
spa_log_jam = Image.open("./Images/Spa_Log_Jam.png")
spa_alpines = Image.open("./Images/Spa_Alpines.png")
china_circuit = Image.open("./Images/China_Circuit.png")
chinasprint_erick_patrick = Image.open("./Images/ChinaSprint_Erick_Patrick.png")
chinarace_incident = Image.open("./Images/ChinaRace_Incident.png")
chinarace_eddie_boz_incident = Image.open("./Images/ChinaRace_Eddie_Boz_Incident.png")
chinarace_erick_mistake = Image.open("./Images/ChinaRace_Erick_Mistake.png")
baku_circuit = Image.open("./Images/Baku_Circuit.png")

def Tab0():
    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False
    
    #region Race Week Baku
    st.subheader('Race Week - Baku')
    st.markdown('''
                It has been an eventful few days since the league’s first Sprint race. A major FIA decision was made that changed the results of the race, and let’s just say there has not been this much rioting since the 1991 Chicago Bulls celebration riots. Some drivers put pen to paper to rip into the FIA’s decision for being abrupt and unfair. While other drivers defended the decision as it upheld aspects of racing sportsmanship they appreciate. Alpine’s start driver Joshua ended his tirade by saying:

                > _**This is really BS and unfair.** - Joshua_
                
                The next day, Joshua spoke to a local reporter and stated:

                > _**Everyone better watch out because we are coming for blood [in Baku]. [The decision is] Not fair but we move forward.** - Joshua_

                His teammate Eddie took an interview with a Houston based reporter where he labelled the FIA as blind while elaborating on the situation between he and Joshua:

                > _**While yes I do admit to running Josh off the road, which I did get a penalty for on top of my other 5-grid penalty (which resulted in me having a 10-grid penalty already), Joshua also got a 5-grid penalty from that for no exact reason. Due to the FIA not having eye balls, Joshua already had to push harder and try stupider sh*t just to make it back to his true position, P1. This all resulted in his situation during the Sprint race. He should not be penalized further, when he was already penalized and is getting penalized for a rule which was never stated before the race.** - Eddie_

                Other drivers like the VCARB pair were more ceremonious and in agreement with the FIA’s decision. Patrick was heard screaming, “I’m a winner!” as far away as Erick’s house. The shouts were measured on local seismology equipment as a 3.2 magnitude earthquake on the Richter Scale. His teammate Brently was more subdued with his commentary stating:

                > _**I feel like it was the right decision. As it seemed odd when and where he retired [in the Sprint].** - Brently_

                Multiple teams have also released formal statements which can be found at the end of this article. More importantly, this ruling shakes up the standings quite a bit. Joshua dropped below McLaren’s Nick in the Driver’s Championship and VCARB closed even further on McLaren in the Constructor’s Championship.

                With all this said, it’s time to focus on the upcoming street race in Baku. Drivers will be met with close walls, the longest pedal to the medal straight on the calendar, and deviously challenging combinations of undulation and corners. Sector 1 is essentially three flatout straights with ninety-degree left turns at the end of each. If drivers survive that, they will quickly find themselves at the beginning of the most challenging sector on the league’s calendar. The castle section and Turn 15 have caught out many talented drivers before and are certainly capable of wreaking havoc on the race this week. Sector 3 is a drafters paradise, but the exit of Turn 16 will make or break any challenger’s attack on their rivals.
                ''')
    st.image(baku_circuit)
    st.markdown('''
                This will be the league’s first race in Azerbaijan. With plenty of treacherous turns and a great passing opportunity at the end of the front straight, the Baku street circuit will certainly test the league’s fortitude. Especially when one considers the embers that are ready to be stoked by even the slightest breeze from China’s incident.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Saturday 1/11/2025 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)
    st.markdown('''
                **Official Team Statements**
                ''')
    
    china_statements = [
        {
            "title": "",
            "text": "",
            "img": "./Images/China_Alpine_Statement.png"
        },
        {
            "title": "",
            "text": "",
            "img": "./Images/China_Red_Bull_Statement1.png"
        },
        {
            "title": "",
            "text": "",
            "img": "./Images/China_Red_Bull_Statement2.png"
        },
        {
            "title": "",
            "text": "",
            "img": "./Images/China_VCARB_Statement.png"
        },
        {
            "title": "",
            "text": "",
            "img": "./Images/China_Ferrari_Statement.png"
        },
    ]
    
    carousel(china_statements)
    st.divider()
    #endregion
    
    #region FIA China Press Release
    st.markdown('''
                **Press Release** \n
                **For Immediate Release**  
                _Date: January 10 2025_
                ''')
    st.subheader('Joshua Penalized with Five-Place Grid Drop Following Sprint Race Incident at the F124 League’s Chinese Grand Prix')
    st.markdown('''
                The Alternative F124 League’s independent FIA directors have issued a decision regarding an incident that occurred during the recent Chinese Grand Prix, resulting in a five-place grid penalty for driver Joshua. 

                Following an extensive review of race footage and telemetry data, it has been determined that Joshua retired his car during the sprint race despite no terminal damage, with the intention of improving his starting position for the main race—set to be held in reverse order of the sprint race results. This behavior was deemed to be in violation of league regulations.

                In comparison, Patrick, who also sustained damage during the sprint, made the decision to repair his car and continue racing, ultimately putting in a solid performance to finish the race.

                As a result of the penalty, Joshua will drop from 1st to 6th in the final results. The revised finishing positions from the Chinese Grand Prix are as follows:

                - 1st: Patrick  
                - 2nd: Erick  
                - 3rd: Nick  
                - 4th: Eddie  
                - 5th: Boz  
                - 6th: Joshua  

                Joshua has the right to appeal this decision to the independent FIA directors, David and Marcus, should he wish to contest the ruling. The Alternative F124 League remains committed to upholding fair and competitive racing for all participants.

                For further inquiries or clarification, please contact Erick Tavera or Nick Beglin.
                ''')
    st.markdown('''
                <div style="width: 25%; border-bottom: 1px solid #cccccc;"></div>
                ''', unsafe_allow_html=True)
    st.markdown('''
                _The Alternative F124 League_
                <p style="color:lightgray;">Where racing meets integrity and fair competition.</p>
                ''',
                unsafe_allow_html=True,)
    st.divider()
    #endregion

    # "Show More/Less" button 
    if not st.session_state.show_all_content:
        if st.button('Show More'):
            st.session_state.show_all_content = True
            st.rerun()  # Rerun the app to show everything
    else: 
        if st.button('Show Less'):
            st.session_state.show_all_content = False
            st.rerun()

    if st.session_state.show_all_content: 
        #region China Recap
        st.subheader('China Recap: Overtakes, Incidents, and Revenge Oh My!')
        st.markdown('''
                    There was a buzz around the Paddock (Discord) on Wednesday as the drivers prepared for the first Sprint in league history, and the first of three Sprints scheduled for this season. The abbreviated qualifying sessions led to a new pole sitter for the Sprint, with VCARB’s Patrick setting the pace. McLaren’s Nick took the other slot on the front row after current Driver’s Championship leader, Alpine’s Joshua, saw a five place grid penalty drop him to sixth. Once the lights were out, the driver’s sprung to life and cruised through the first few corners of the track. Coming out of Turn 6, Nick took the lead of the race after a small racing incident. There was no looking back for him after that as he built a substantial gap and took home the win, while Nick’s gap built, Patrick battled back from the incident, but ended the race in 18th due to what can only be described as a calculated bit of revenge from Ferrari’s Erick who closed the door on him into Turn 1.
                    ''')
        st.image(chinasprint_erick_patrick)
        st.markdown('''
                    Other noteworthy outcomes of the Sprint include Joshua being unable to keep it between the white lines with his fancy new racing wheel, and VCARB’s Brentuar taking home his first podium of the season. At the conclusion of the Sprint, Red Bull’s Boz had overtaken McLaren’s Travis and Alpine’s Eddie had brought it even with Ferrari’s Zane in the Driver's standings. The podium for the Sprint saw Nick celebrating on the top step, Erick one step down, and Brently on the third step.

                    Once the dust had settled on the track from the Sprint, the drivers lined back up in reverse order from the results of the Sprint for the main event. This saw Joshua starting second next to George Russell who had also DNFed during the Sprint. Chaos ensued throughout the race as contenders started on the back row and were forced into making daring passes to make up ground on Joshua. From crazy maneuvers off the starting line to more Turn 6 shenanigans, drivers were pushing to the limit of the rules and what the cars can provide to make up ground early. Nick was a big winner early on in the race, but Erick was also able to make up ground throughout the first stint. It was clear that two major strategies were in play. For the front runners, a two stop plan was the consensus and for those starting in the back a one stop strategy allowed them to extend and make up places against the two stoppers.
                    ''')
        st.image(chinarace_incident)
        st.markdown('''
                    As the race went on, the hairpin at the end of the back straight saw multiple incidences. First there was a double spin out that saw Boz and Alpine’s Eddie slam into their opponents causing four cars to split open like the Red Sea, allowing Erick to make up those places in a single corner.
                    ''')
        st.image(chinarace_eddie_boz_incident)
        st.markdown('''
                    However, Erick was not done with participating in dramatic moments in Turn 14’s hairpin. As the race continued and tire strategies began to play out. Front runner Patrick came out of the pit behind a battling duo of Nick and Erick. As the duo went through the hairpin for a second time, Patrick was close enough to make a move on Erick. With this in mind, Erick attempted to pull off an overtake on Nick to slow the incoming attack from behind. However as the hairpin approached and braking began, Erick pulled out of his attack and caused himself to brake too late and into the runoff. This allowed the other two drivers in the battle to move onto the front straight where Nick would eventually give way to the fresher tires on Patrick’s VCARB.
                    ''')
        st.image(chinarace_erick_mistake)
        st.markdown('''
                    While some drivers were calling for an end to the reverse grid format, the results of the race might be the most spectacular for the league all season. Drivers like Boz, Eddie, and Patrick saw their best finishes of the season in the main race. Additionally, spectators were given a show of talent as the drivers completed the most overtakes of the season, nearly doubling the total number of overtakes from all the previous races combined. With this in mind league officials have begun devising ways to mitigate the complaints of the format, while still allowing for the epic conclusions it provided.

                    With every car across the line, Joshua took home another win, with Patrick and Erick just behind. Nick crossed in third, but due to penalties acquired while overtaking the backfield he ended up falling to Erick who was just a few seconds behind. The Driver’s Championship saw VCARB teammates swap places, while the Constructor’s Championship saw the VCARB outfit grow ever closer to jumping into second place. The final standings of the race also included a first for the league. This is the first race where the league’s drivers finished in the top places consecutively without AI players in the mix. All-in-all an incredible outing full of high energy, a tasteful bit of cyberbullying, and stellar driving performances. Next week the league takes on the streets of Baku which may prove to be the most challenging race of the season.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 1/9/2025 - Patrick Knowles with credit Erick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion
        
        #region Race Week China
        st.subheader('Race Week - China')
        st.markdown('''
                    The league’s relentless schedule continues this week in China. Home to the third longest straight on the league’s calendar, Shanghai Audi International Circuit will allow drivers to overtake at high speed as well as through twisting and daring low and medium speed turns. Both straights include DRS zones which should enable thrilling wheel to wheel action in both the sweeping Turn 1 & 2 combination as well as Turn 14’s hairpin.
                    ''')
        st.image(china_circuit)
        st.markdown('''
                    While the circuit has many twists and turns, the biggest twist for the league is the week’s format. Not only will a standard race occur on Wednesday, the league will face its first ever Sprint race. If that wasn’t enough, league officials have devised an exciting plan to bring some variety to the race week. Drivers will face a standard three session qualifying to help set the grid for the Sprint. From there the drivers will complete a short stint of laps around the circuit at full tilt to score points. The results of the Sprint race will be used to set the grid order for the race, in reverse. That’s right, qualifying, Sprint, and the main race grid set in reverse off of the results of the Sprint. The format is sure to force drivers into daring passing scenarios, fingers crossed everyone keeps it between the white lines.

                    So how much does this race matter? With the added 8 points available from the Sprint race, the Driver’s Championship can turn topsy-turvy, especially with the added suspense of the reverse grid. With respect to the Constructor’s Championship, nearly every team has the ability to make up ground or even leap-frog the current leader. As we adjourn this race week update, let’s take a look at the results of yesteryear. Last season saw McLaren’s Nick take home the win, with the then Mercedes driver, now Aston Martin driver, Del stepping up to the second step of the podium, and the then Red Bull driver, now Ferrari driver, Zane bringing home third. However, with two wins up for grabs and the new format almost anything is possible.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Sunday 1/5/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Spa & Spain
        st.subheader('Spa & Spain Recap: Two Tracks, Tons of Turmoil, and Terrible Teamwork')
        st.markdown('''
                    Buckle your helmet straps, pull up your gloves, and button your firesuits, because this recap is juicy. First we will cover the results of the races. Then we will take a trip down turmoil lane to unpack the dramatic happenings of the double header. Finally, we will highlight the evening’s attempted works of teamwork.
                    ''')
        st.image(spain_cover)
        st.markdown('''
                    **Two Tracks**
                    
                    Drivers took on two high speed, long, and arduous tracks. First, the league started at Spa where a surprise qualifying occurred with both Kick Sauber cars out pacing all of the drivers by leaps and bounds. However, neither Kick car was able to fend off the league’s drivers for more than a few laps. As the race continued a few safety cars brought the field together which allowed McLaren’s Nick to take home his second win of the season, with Alpine’s Joshua coming in second, and Aston Martin’s Del taking home his second podium of the season. Notably, both Del and VCARB’s Brently made up multiple places over the course of the race. After the race the midfield standings saw a few changes. In the Constructor’s Championship VCARB overtook Ferrari. While in the Driver’s Championship Brently overtook VCARB’s Patrick, Del overtook Ferrari’s Zane, and Red Bull’s Boz separated from Aston Martin’s Gary.

                    After a quick break the league strapped in for 33 laps in Barcelona, Spain. Qualifying saw Nick outpace Ferrari’s Erick by a thin margin. However at the end of the race, Joshua ended up taking home the victory, with Nick just behind, and Erick rounding out the podium. Just like in Spa, the race was full of turmoil but also a notable performance by Red Bull’s Yeti. Starting in 14th, Yeti ripped through the field, passing nearly every contender and battling all the way up into 5th place for his best finish of the season. Yeti’s notable performance resulted in the only change in the championship standings, with him overtaking Zane.
                    ''')
        st.image(spain_yeti)
        st.markdown('''
                    **Tons of Turmoil**

                    With the important updates out of the way, let’s get into the drama from the double header. First and foremost, the FIA was under fire again with numerous penalties granted to drivers in Spa for exceeding track limits. So much so, and to the delight of corner cutters everywhere, the regulators decided to loosen up on their penalty calls while in Spain.

                    With plenty of penalties awarded for track limits, the FIA was surprisingly quiet when it came to penalizing aggressive drivers who ran their competitors off track. Right out of the gate in Spa, Joshua took an assertive position on the exit of Turn 1, forcing Nick off track on their way down to Eau Rogue. Within the next lap, Joshua chose to slow down and allow Nick to pass in a gesture of good faith and motor-sportsmanship. Unfortunately, this was not the only incident where a driver ended up off track. While battling, Erick began an attack on Patrick on the outside of the main start-finish straight. Patrick, unaware of how far Erick had advanced, held his line, and forced Erick to take drastic actions on the grass and gravel runaway of Turn 1. After review, neither incident was deemed sufficient enough for further penalty to any driver.
                    ''')
        st.image(spa_nick_joshua)
        st.markdown('''
                    Spa also delivered two extraordinarily long safety cars. The first was caused by Erick losing control at the top of Eau Rogue. Nearly all the drivers immediately pitted for new tires and queued up behind the insanely erratic safety car. Alpine’s Eddie found himself in front of his teammate Joshua and attempted to provide a meaningful position swap at the restart, more on this later. This maneuver, along with a poorly contrived passing attempt by Patrick, ended with another safety car after Patrick accidentally pit maneuvered Yeti, log jamming the whole field (except Erick who made up 12 places in one turn).
                    ''')
        st.image(spa_log_jam)
        st.markdown('''
                    Safety cars were a theme in both races. While in Spain the drivers faced a relatively early safety car at the end of Lap 13. Many drivers pitted, and committed to tire saving throughout the race. The restart was mostly uneventful with nominal slipstream passes and great battles due to the grouped up drivers. One such battle occurred between Nick, Patrick, and Erick headed into La Caixa at the beginning of Sector 3. In what can only be described as an act of vengeance, Erick forgot to brake and nearly sideswiped Patrick and t-boned Nick. However, he gently grazed both drivers and neither incurred any damage.

                    Spain ended with one last bit of turmoil as Joshua began to tout his fastest lap streak. Conveniently, Patrick was on a two stopper with his final stint on the soft compound tires. With a full battery, fresh tires, and fuel low, Patrick changed his engine mode and pushed, securing the fastest lap of the race for the moment. In spite of the time set, a pair of teammates were determined to try and take the fastest lap, more on this later.

                    **Terrible Teamwork**

                    While not terrible, a few teammates were unable to race one or both races which resulted in some of the standings changes mentioned previously. But, remarkably terrible teamwork came out of the French outfit in both races. While lapping through the Ardennes Forest, Joshua ended up behind Eddie during the first safety car. The two conjured up the idea to let Joshua by on the shortest straight of the track coming out of the slowest corner on the track. This failed miserably as Joshua jumped the gun and Eddie forgot where his accelerator was. Causing Yeti, Patrick, Joshua, and Eddie to be 4-wide coming across the DRS activation line. The league watched it back like an end of year fail recap from a mildly unsuccessful sim racing streamer. Laughs were shared, teammates yelled at one another, and it felt like we were back at the Christmas Eve dining table listening to family debate meaningless politics, knowing full well how silly the whole scenario is.

                    Now if that were the only silly teammate moment, this article would be done. But, as you can see, it isn’t. As previously mentioned Joshua had won the fastest lap award at every single race this season. But in Spain, Patrick had a prime opportunity to snag a fastest lap near the end of the race. Joshua, afraid to lose his victory, did not pit and try to retaliate, instead, he had his teammate Eddie pit and attempt to snag the fastest lap. They tried new tires, slipstreaming, and what some are calling “coaching,” but to no avail. Joshua’s streak ended and on the last lap the Alpine pair were at each other’s throats.
                    ''')
        st.image(spa_alpines)
        st.markdown('''
                    The league takes on China next week in the first Sprint race in league history. There are sure to be fireworks as regulations are set to change back to strict for exceeding track limits and the new Sprint format is bound to cause some sort of drama.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 1/2/2025 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Spa & Spain
        st.subheader('Race Week - Spa & Spain')
        st.markdown('''
                    Motorsports fans are in for a treat. The league is kicking off the New Year with a double feature: Spa Part 2 Electric Boogaloo followed by high speed thrills in Barcelona Spain. As the perils of Spa have been covered in a previous post, this will focus on Spain and its high speed twists and turns. Track limits, tire wear, and plenty of places for aggressive overtakes should all combine for an unpredictable event. 
                    ''')
        st.image(spain_circuit)
        st.markdown('''
                    Once the lights go out the drivers will have a long straight to draft, bump, and position themselves for the first pair of corners. Both are wide enough to allow for drivers to go two or even three wide for the brave. The third corner will require incredible courage for the drivers to be wheel to wheel throughout, but during the first lap who knows what might happen. Sector 2 will help queue up the drivers for the circuit’s back straight. If everyone’s wings, wheels, and side pods are still intact, the drivers will need to test the track limits on their way to the final corner at full tilt. With two DRS straights, there will be plenty of room for conventional overtaking. However, with sweeping high speed and medium speed corners, the circuit will allow for harrowing battles throughout each lap. 
                    ''')
        st.markdown('''
                    The drivers will need to respect the track limits both for penalty's sake as well as the heavy amount of gravel that lines the high speed portions of the circuit. Penalties, crashes, and yellow or red flags all could lead to some incredible shifts in the standings. Drivers will also have to battle through the fatigue of the day’s double header. Which they did not have to contend with the last time out in Spain. That outing provided a close race between McLaren’s defending champion Nick and the then Mercedes driver, now Ferrari driver, Erick with the other Ferrari brother, then Aston Martin driver, Zane rounding out the podium. Three of the league’s drivers DNS and two of the AI DNF. Spain should provide plenty of exciting racing for every driver who makes it to the starting line.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Saturday 12/29/2024 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Spa Update
        st.subheader('Spa Update')
        st.image(postponed)
        st.markdown('''
                    The league’s battle at Spa has been postponed until 1/1/2025 or later. Something about some driver ditching to party in Mexico and a few drivers unable to connect to EA's crappy servers. However this did allow some of the drivers to run some laps in Saudi Arabia as a mid-season practice session. The FIA will be working to finalize the upcoming schedule for the remainder of the season as rumor has it there will be a week or two of double headers. The league takes a short break as we head into this holiday season to allow drivers to recuperate and spend time with loved ones.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Saturday 12/22/2024 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Spa
        st.subheader('Race Week - Spa')
        st.markdown('''
                    The league heads out for a Spa day this week. However, this one probably won’t be all that relaxing. With the Constructor’s and Driver’s championships heating up, Spa will prove to be a place where everyone has the opportunity to make up ground. Historically known as a track favorable for overtaking, Spa’s sacred pavement is also known for being one of the most treacherous high-speed circuits on the calendar. Nestled deep in the Ardennes forest, Spa is riddled with corners, straights, and stories that have filled the racing history books.
                    ''')
        st.image(spa_circuit)
        st.markdown('''
                    Famous early corners like La Source and Raidillon’s Eau Rogue will provide exhilarating braking and high-speed moments. Followed by the twisting turns of Le Combes, Pouhon, and Campus among others, the drivers are sure to provide incredible wheel-to-wheel action. Finally drivers will have the opportunity for late sends or strategic tailgating going into the chicane before the start-finish straight.
                    ''')
        st.image(spa_collage)
        st.markdown('''
                    Previously when the league navigated a day at Spa, McLaren’s Nick took home the win. He finished just seconds before the then Mercedes driver, now Aston Martin driver Del. While Ferrari’s Erick rounded out the podium. Current league leader, and Alpine driver, Joshua was unable to start the race along with three other drivers. In fact, Joshua has not run a race at Spa in the last two seasons, and reigning champion Nick has not lost at Spa in recent memory. Ferrari’s pairing of Erick and Zane have also had historically good races, with Erick boasting a second and third place finish, and Zane placing fourth on his last two outings. With the addition of last week’s regulation changes and the thrilling nature of the Circuit of Spa-Francorchamps, this week is aimed at being another piece of absolute cinema. Hopefully none of the drivers end up just a few tire marbles short of a win.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Saturday 12/14/2024 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Australia Recap
        st.subheader('Australia Recap: A Rumble Down Under')
        st.markdown('''
                    tldr; Australia did not disappoint. Safety cars, front wings destroyed, questionable restarts, engines blown, drivers fuming, DNFs, a DNS, and a new race winner. 
                    '''+'''
                    With race hype at an all time high the drivers jumped into discord and silently sat waiting for the race to begin. Nerves were frayed, but when the lights went green in qualifying the drivers took to the streets of Albert Park without much trouble. The Red Bull pairing failed to make it out of Q1 and Alpine’s #2 driver Eddie totaled his car beyond repair, making it impossible for him to set a lap time during Q2. The final results of Q3 saw Alpine’s Joshua take home another pole position, with McLaren’s Nick, Aston Martin’s Del, and VCARB’s Patrick completing the first two rows. The Ferrari pairing occupied the third row and McLaren’s Travis and VCARB’s Brently rounded out the top eight on the fourth row of the grid. The rest of the field found themselves starting near the back, which to some strategists was the right move to ensure their drivers survived the first corner.
                    ''')
        st.image(australia1)
        st.markdown('''
                    When the five lights went out, the drivers quickly proceeded down the straight into Turn 1 where the top few drivers made it through fairly clean. However, Zane’s Ferrari was caught up in an incident on his way through Turn 2. This ended up proving to be a detrimental loss for Zane early in the race. Erick was able to make up a place into fourth passing Del and avoiding contact through the first few corners. 
                    '''+'''
                    As the race continued Alpine’s dominant driver Joshua took an early lead but was unable to break free from McLaren’s top contender Nick. As the front of the pack continued, Erick miraculously avoided contact with both Patrick and Nick in Turn 3 as he found himself in the gravel. This maneuver would have normally left him high and dry, but an early VSC and safety car allowed Erick to get right back into the groove. 
                    ''')
        st.image(australia2)
        st.markdown('''
                    Track limits were heavily enforced across the field as drivers tested the race director’s new regulations. Prior to the start of the race the league was informed that, due to sloppiness and abuse of the rules by Alpine’s Joshua at Silverstone, any corner cutting would be strictly recorded and penalties would be awarded for drivers who broke the rules three or more times throughout the race. For most these penalties were minor and did not end up changing the outcome of the race. However in the post race driver’s meeting there was a minor uproar that the regulations were too strict. Only time will tell if these regulations will remain or if the race director will renege their stance.
                    '''+'''
                    With just nine laps to go a late safety car bunched up the drivers and allowed some to take advantage of a less impactful pitstop. With Joshua still in first, Nick tailing him, and Erick following in third, the queue of cars cautiously took the final few corners of Lap 22 waiting for Joshua to throttle up. Waiting on bated breath, Nick and Erick pounced as Joshua launched only to find Joshua jump off the throttle for a short moment causing a multitude of front wings to be damaged. Regardless, no penalties were called and the drivers mustered what they could with their damaged vehicles. A tight battle ensued up front which ultimately saw McLaren’s Nick take home his first win of the season with Alpine’s Joshua right behind. 
                    ''')
        st.image(australia3)
        st.markdown('''
                    Rounding out the podium was Ferrari's Erick, who moved up from 5th to 3rd. Just behind him the two VCARB drivers had their best team finish of the season with Patrick finishing 4th, and driver of the day Brently moving up from 8th to 5th. Del was unable to fully recover from the early setbacks and ended in 11th with McLaren’s Travis just behind in 12th, and Alpine’s 7th place wunderkind Eddie falling all the way back to 13th. Rounding out our finishers today was Ferrari’s Zane in 15th. For Red Bull, this will be a qualifying and race to take notes from and improve upon as both drivers ended up unable to cross the finish line. Aston Martin again ran with just a single driver today as Gary was sadly watching the Knicks fall to the Hawks.
                    '''+'''
                    After all the engines were turned off and points totalled, battles for rank in both the World Driver’s and Constructor’s Championships have begun to heat up. McLaren begins to close the gap to Alpine and leap frogs Ferrari into second. In the Driver’s Championship, we saw both of the VCARB drivers overtake Ferrari’s Zane, but the leaders Joshua, Nick, and Erick remain the same. Next our drivers take to the Belgian forest in Spa where they will test their mettle against the highspeed Eau Rouge and longest track on the calendar.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Thursday 12/11/2024 - Patrick Knowles with credit Erick & Nick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Australia
        st.subheader('Race Week - Australia')
        st.markdown('''
                    This week the drivers will be “defying gravity” while racing upside down in Melbourne. The real question is whether or not the league continues to let Alpine and Joshua cook? Or maybe more fittingly, will the league let Joshua put another shrimp on the barbie? Only the streets of Albert Park will be able to answer these questions.
                    '''+'''
                    Albert Park Circuit provides the first street circuit of the year, which without a doubt is set to create some sparks. With the first heavy braking Turn 1 of the calendar, the start of this race will likely turn into an abbreviated game of Survivor. From there the drivers will be challenged by tight walls coming out of Turn 2 and Turn 5 as they queue up into the highspeed Sector 2. Sector 3’s heavy braking zones will provide tantalizing opportunities for the drivers to throw dummies, lick it and send it, and hopefully keep all the carbon fiber on their cars
                    ''')
        st.image(australia_circuit)
        st.markdown('''
                    The league took a short pause from running down under last season. Which means the most recent winner here is current Ferrari driver and previous Mercedes driver Erick, who took home a commanding win with a lead of 18 seconds over McLaren’s Nick. Rounding out the podium was  retired Mercedes driver turned steward Marcus. If Silverstone’s race is any evidence of how close the drivers plan to race this week, we will certainly see an exciting race in the capital of Victoria. With nearly no room for run off, mistakes will be magnified, and incidents are sure to become heated.
                    '''+'''
                    <p style="color:lightgray;">Saturday 12/7/2024 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,
                    )
        st.divider()
        #endregion

        #region Silverstone Recap
        st.subheader('Silverstone Recap: “007 You Only Win Twice”')
        st.image(silverstone0)
        st.markdown('''
                    Another week, another race. The sun mercifully shone down on the British Isles and provided the perfect weather for an eventful race. Reigning WDC Nick, and Alpine’s top driver Joshua, battled it out for 26 laps straight. Joshua took the win after a little bit of questionable contact and a helpful dose of backmarker blocking. This is Alpine and Joshua’s second win of the season. Alpine also had some 007 magic from their second seat, Eddie, who had 0 intention of racing, 0 practice, and placed 7th. Coincidentally this was also his second time placing 7th this season. Let’s see if this pattern continues for the French outfit.
                    ''')
        st.image(silverstone1)
        st.markdown('''
                    The podium was rounded out by Ferrari ace, Erick, who raced a lonely set of laps around the hallowed airfield. Ferrari’s other driver Zane battled with VCARB’s Patrick in a tightly contested tango where the drivers had opposite tire strategies (softs to mediums and mediums to softs respectively). However, in the end, a bit of contact left Zane just out of reach on the final lap.
                    ''')
        st.image(silverstone2)
        st.markdown('''
                    Further down the field the two Red Bull drivers Yeti and Boz sparred for the entire race, ending in 6th and 11th after a late error by Boz. Which allowed VCARB’s Brently to make up a place after a muddled start, and end in 8th. Finally, rounding out our grid this week were the Aston Martins with Gary finishing in 19th and Del MIA for this week’s bout.
                    '''+'''
                    Alpine’s Joshua takes an early strong lead in the WDC with his back-to-back wins. His efforts, along with Jr.'s, have propelled the team into the lead for the WCC as well. As it stands today Alpine leads the way, followed by Ferrari and McLaren who are separated by mere points. The WDC currently stands with Joshua, Nick, and Zane in the top three with Erick just one point behind his Ferrari teammate in 4th. See you all down under where the league takes to the converted streets of Albert Park.
                    ''')
        st.markdown('''
                    <p style="color:lightgray;">Wednesday 12/4/2024 - Patrick Knowles with credit Eddie & Nick</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Race Week Silverstone
        st.subheader('Race Week - Silverstone')
        st.markdown('''
                    Rise and shine gamers, its race week! This week The Alternative will take to the famed and hallowed pavement of Silverstone. With a week off for the Thanksgiving holiday, the drivers should not be worried about meeting the minimum weight limit at the end of the race. With the season still young, all drivers are still hopeful they can make a meaningful impact on both championship races.
                    '''+'''
                    Additionally, the league’s president, Mr. Erick Tavera, is proud to unveil the crown jewel of this year’s competition, the champion’s trophy. Derived from F1’s cancelled COTA trophies, The Alternative’s World Driver’s Champion and Constructor’s Champions will receive a commemorative trophy marking their achievement from throughout the season. The Pirelli tire the champion stands upon has each of this season’s tracks encircling the perimeter of the tire. The races won by each driver or constructor will be highlighted in gold. Additionally, the bottom of the base will include the driver’s and constructor’s records and accomplishments from throughout the season.
                    ''')
        st.image(trophy)
        st.markdown('''
                    <p style="color:lightgray;">Sunday 12/1/2024 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        st.divider()
        #endregion

        #region Suzuka Recap
        st.subheader('Suzuka & Pre-Season Recap')
        st.markdown('''
                    With a lovely pre-season in Miami complete where 8 of the league's 12 drivers and all 6 constructors took to the streets around Hard Rock Stadium, the lights went out in Suzuka to an aborted start. With a multiple car incident that sent the whole grid into turmoil,the race director determined it was best to have a full restart. One of our top qualifiers, VCARB's Patrick, fell back two positions at the start and near the end of the first lap attempted to make up those positions going into the Hitachi Astemo Chicane. This maneuver failed and ended with a slow down into the chicane allowing many of our drivers to make up spots against the AI and other drivers. The remainder of the race saw only a few spins, beachings, and other minor mishaps that affected a few of the final standings. Big winners from this race include VCARB's Brentuar as well as Aston Martin's Del. Alpine's Joshua took home the win and the fastest lap with McLaren's reigning champion Nick coming in second and Del rounding out the podium.
                    ''' + '''
                    With the results final, Alpine takes an early lead in the Constructors’ Championship. Alpine's Joshua is also leading the Driver's Championship. Reigning champion Nick finds himself in second place in the Driver's Championship with his team, McLaren, also slotting into second overall in the Constructors’ Championship. Ferrari, Aston Martin, VCARB, and Red Bull respectively make up the rest of the Constructors’ Championship standings.
                    '''+'''
                    <p style="color:lightgray;">Thursday 11/21/2024 - Patrick Knowles</p>
                    ''',
                    unsafe_allow_html=True,)
        #endregion