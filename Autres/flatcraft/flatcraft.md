# Flatcraft – Village Generation & Loot System

## Java – 2D Sandbox – Solo Project – 2022

Flatcraft was a school project where we were handed the source code for a simple 2D Minecraft-inspired game and tasked with expanding its features. The original base was fairly barebones: a flat, tile-based world with basic terrain generation (grass, trees, ores), grid-locked player movement, and simple crafting and smelting systems. The player was represented by the tool they held, and movement felt stiff and primitive.

My contribution was the design and implementation of a fully functional village generation system with randomized loot chests, all created from scratch. I structured village spawning around the trees already placed in the world. When generating a region, the system would randomly choose between three outcomes: no village, a small village (3 houses), or a larger one (5 houses). Each house had one of three possible layouts, each with different chest positions and a random chance for each chest to actually appear.

For the loot system, I created a pool of resources and tools. When a chest was generated, it would select random item IDs and assign small quantities (e.g., under a dozen), with variation depending on the item type. The idea was to give players a reason to explore villages without breaking the game balance.

One of the biggest challenges I faced was making sure each chest functioned as a unique entity. At first, all chests behaved like shared storage—a side effect of the base game being poorly designed to support such systems. Overcoming that limitation involved carefully separating inventory data and ensuring state persistence per chest. This was in part because we were asked to modify the base code as little as possible so that integrations with the other projects could be done easily.

Although all visuals were provided (and later traced back to the open-source project Minetest), I focused entirely on the logic and structure of the systems. The entire feature was coded solo over the course of a few months in the second semester of the 2021/2022 school year.

Despite the rough foundation we were given that many struggled to work with due to it being overly convoluted and confusing. I’m proud of the entire feature I built. If I were to revisit the system today, I’d likely refactor some of the code for clarity and modularity, but the core ideas and implementation remain solid and functional.