--creating the service
Players = game:GetService("Players")
--PlayerAdded : Fire when player enters the game
-- :Connect(function(something)) or : Connect(function)
Players.PlayerAdded:Connect(function(player) 

    -- printing starter joining
    print(player.Name .. " joined the game!")

    local folder = Instance.new("Folder", player)
    folder.Name = player.Name

end)

Players.PlayerRemoving:Connect(function(player)
    -- printing when stop game
    print(player.Name .. " left the game!")
end)

local function onPlayerAdded(player)
    print(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local points = Instance.new("IntValue")
    points.Name = "Points"
    points.Value = 0
    points.Parent = leaderstats
end
Players.PlayerAdded:Connect(onPlayerAdded)

-- Healthing Score
local MAX_HEALTH = 100
local ENABLED_TRANSPARENCY = 0.4
local DISABLED_TRANSPARENCY = 0.9
local COOLDOWN = 10

local healthPickupsFolder = workspace:WaitForChild("HealthPickups")
local healthPickups = healthPickupsFolder:GetChildren()

local function onTouchHealthPickup(otherPart, healthPickup)
    if healthPickup:GetAttribute("Enabled") then

        local playerList = Players:GetPlayers()
            for i = 1, #playerList  do
                local player = playerList[i]
                if player then
                    local points = player.leaderstats.Points
                    points.Value = points.Value + 1
                end
            end

        local character = otherPart.Parent
        local humanoid = character:FindFirstChildWhichIsA("Humanoid")
        if humanoid then
            print(humanoid)
            humanoid.Health = MAX_HEALTH
            healthPickup.Transparency = DISABLED_TRANSPARENCY
            healthPickup:SetAttribute("Enabled", false)
            task.wait(COOLDOWN)
            healthPickup.Transparency = ENABLEDTRANSPARENCY
            healthPickup:SetAttribute("Enabled", true)
        end
    end
end

for , healthPickup in ipairs(healthPickups) do
    healthPickup:SetAttribute("Enabled", true)
    healthPickup.Touched:Connect(function(otherPart)
        onTouchHealthPickup(otherPart, healthPickup)
    end)
end