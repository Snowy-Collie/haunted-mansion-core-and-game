import json
import random
import csv
import os
def generate_game():
    callsigns = []
    with open('./Airlines.csv', mode='r', encoding='utf-8') as f:
        r = csv.reader(f)
        for i in r:
            callsigns.append(i[2])
    callsigns.pop(0)
    flight_no = f"{random.choice(callsigns)}{random.randint(100, 999)}"
    apt = []
    with open('./Airports.csv', mode='r', encoding='utf-8') as f:
        r = csv.reader(f)
        for i in r:
            apt.append(i[4])
        apt.pop(0)
    dep_apt = random.choice(apt)
    game_list = []
    T_F = 1500 # Total Flights
    S_P_F = 6 # Step per flight
    EA_START_IDX = (T_F * S_P_F) + 1
    EB_START_IDX = EA_START_IDX + 4
    RETIRE_IDX = EB_START_IDX + 4
    QUIT_IDX = RETIRE_IDX + 1
    game_list.append([
        f"[Narrator]: Welcome Captain. You are in the cockpit of Flight {flight_no} at {dep_apt}. Pre-flight checks are complete.",
        [["Request ATC Clearance", 1], ["Perform Engine Start", 1], ["Request Pushback", 1]]
    ])
    for i in range(1, T_F + 1):
        rwy = str(random.randint(1, 36))+random.choice(['L', 'R', 'C',""])
        current_idx = len(game_list)
        if i != 1:
            flight_no = f"{random.choice(callsigns)}{random.randint(100, 999)}"
        game_list.append([
            f"[ATC - Delivery] [Flight {i}/{T_F}]: '{flight_no}, cleared to destination as filed. Squawk {random.randint(1000, 7000)}.'",
            [["Read back and confirm", current_idx + 1], ["Ignore ATC and Taxi", EA_START_IDX], ["Request different runway", current_idx + 1]]
        ])
        game_list.append([
            f"[ATC - Ground]: '{flight_no}, taxi to holding point Runway {rwy} via taxiway Alpha.'",
            [["Taxi as instructed", len(game_list) + 1], ["Taxi to wrong runway", EA_START_IDX], ["Speed on taxiway", EA_START_IDX]]
        ])
        game_list.append([
            f"[ATC - Tower]: '{flight_no}, Runway {rwy}, cleared for takeoff. Wind {random.randint(1, 360)} at {random.randint(0, 25)} knots.'",
            [["Take off", len(game_list) + 1], ["Abort Takeoff", EA_START_IDX], ["Hold on runway", EA_START_IDX]]
        ])
        game_list.append([
            f"[ATC - Departure]: '{flight_no}, radar contact. Climb and maintain FL350. Contact Radar on 121.5.'",
            [["Climb to FL350", len(game_list) + 1], ["Maintain low altitude", EB_START_IDX], ["Turn off transponder", EB_START_IDX]]
        ])
        rwy = str(random.randint(1, 36))+random.choice(['L', 'R', 'C',""])
        game_list.append([
            f"[ATC - Approach]: '{flight_no}, descend to 3000ft. Cleared for ILS approach Runway {rwy}.'",
            [["Descend and land", len(game_list) + 1], ["Ignore altitude restriction", EB_START_IDX], ["Execute low pass", EB_START_IDX]]
        ])
        if i < T_F:
            dep_apt = random.choice(apt)
            game_list.append([
                f"[Narrator]: Flight {i} completed successfully. You rested for 15 hours at the crew hotel. Ready for the next shift?",
                [[f"Start Next Flight at {dep_apt}", len(game_list) + 1], ["Resign from airline", QUIT_IDX]]
            ])
        else:
            game_list.append([
                "[Narrator]: This is the end of your 1500th flight. You slowly taxi to the gate for the final time.",
                [["Make the final radio call", RETIRE_IDX]]
            ])
    game_list.append([
        "[ATC - Ground]: 'STOP IMMEDIATELY! YOU ARE NOT AUTHORIZED! Airport police are intercepting!'",
        [["Surrender", len(game_list)+1], ["Resist co-pilot", len(game_list)+2]]
    ])
    game_list.append(["[Ending]: Your co-pilot took control. Your license is revoked by the FAA. GAME OVER.", []])
    game_list.append(["[Ending]: You were arrested by Airport Police upon arrival at the gate. GAME OVER.", []])
    game_list.append(["[Ending]: Military vehicles blocked your path. You are removed from duty. GAME OVER.", []])
    game_list.append([
        "[ATC - Radar]: 'UNIDENTIFIED AIRCRAFT, TURN LEFT IMMEDIATELY OR YOU WILL BE ENGAGED!'",
        [["Comply now", len(game_list)+1], ["Fight for control", len(game_list)+2]]
    ])
    game_list.append(["[Ending]: You landed safely but were met by federal agents. License revoked. GAME OVER.", []])
    game_list.append(["[Ending]: Two F-35 fighter jets have locked onto your aircraft! Forceful landing required. GAME OVER.", []])
    game_list.append(["[Ending]: You lost control of the aircraft during the struggle. GAME OVER.", []])
    game_list.append(["[Narrator]: CONGRATULATIONS! You completed 1500 flights. ATC says: 'Thank you for your service, Captain!' The passengers are giving you a standing ovation!", []])
    game_list.append(["[Ending]: You resigned early. Your career ends here, but you are safe.", []])
    if not os.path.exists('games'):
        os.makedirs('games')
    with open('games/pilot_game_en.json', 'w', encoding='utf-8') as f:
        json.dump(game_list, f, indent=4)
    print(f"Success! Generated English JSON with {len(game_list)} nodes.")
if __name__ == "__main__":
    generate_game()