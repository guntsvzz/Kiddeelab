local Players = game:GetService("Players")

local function onCharacterAdded(character, player)
	player:SetAttribute("IsAlive", true)
	local humanoid = character:WaitForChild("Humanoid")
	humanoid.Died:Connect(function()
		local points = player.leaderstats.Points
		points.Value = 0
		player:SetAttribute("IsAlive", false)
	end)
end

local function onPlayerAdded(player)
    -- create a new Folder object using Instance.new() : enabling to create new object within a script
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player

	local points = Instance.new("IntValue")
	points.Name = "Points"
	points.Value = 0
	points.Parent = leaderstats

	player:SetAttribute("IsAlive", false)

	player.CharacterAdded:Connect(function(character)
		onCharacterAdded(character, player)
	end)
end

Players.PlayerAdded:Connect(onPlayerAdded)

while true do
	wait(1)
	local playerList = Players:GetPlayers()
	for i = 1, #playerList  do
		local player = playerList[i]
		if player:GetAttribute("IsAlive") then
			local points = player.leaderstats.Points
			points.Value = points.Value + 1
		end
	end
end