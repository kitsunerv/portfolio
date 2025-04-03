# Ambulance Simulator – AI Management Game

## Unreal Engine 5 – Solo Project – 2024

This project was originally built to meet a school brief: create a small game where ambulances respond to victims randomly scattered around a city. I took the core idea further and turned it into a third-person ambulance management game. The player controls one ambulance, and as the game progresses, can purchase up to three AI-controlled ambulances to help handle the increasing load.

The game is played from a fixed third-person perspective with a clean low-poly aesthetic and a grid-based city layout—all assets and systems were created from scratch by me. There’s no sound implemented yet, but all visuals, UI, and game logic are entirely self-made.

AI ambulances use a custom Dijkstra pathfinding algorithm to locate and transport the nearest accident victim to the closest hospital. 
This is done by using node that are placed at equal distances along the different roads of the city. These connected nodes form a massive (in the current level there are 82 nodes) connected graph that is used for the dijkstra path finding.
The player earns money each time a victim is delivered—either by themselves or by one of their AI units—and can spend that money via a simple UI to purchase additional ambulances. If the player, or ai, aren't quick enought the difficulty can quickly escalates over time as more and more accident victims appear.

One of the biggest technical challenges was implementing Dijkstra’s algorithm with the node system i made. While it generally works well, there’s currently an unresolved bug where AI vehicles occasionally get stuck mid-navigation, which I plan to fix. Despite that, the game is fully playable and already offers a functional gameplay loop.

Looking ahead, I want to introduce rush hour waves where victims spawn at a much higher rate, and add penalty mechanics—such as a timer that causes uncollected victims to disappear, costing the player money. Reaching too many failed pickups would result in a game over, encouraging strategic use of AI units.

This game has been a great playground for blending AI systems, UI design, and simulation mechanics—and a solid solo test of both Unreal Engine and general game design. I'm also really please with the low poly assets i've made for this project as they create this really nice, almost cartoony, vibe.