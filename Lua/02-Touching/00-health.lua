local MAX_HEALTH = 100
local ENABLED_TRANSPARENCY = 0.4
local DISABLED_TRANSPARENCY = 0.9
local COOLDOWN = 10

local healthPickupsFolder = workspace:WaitForChild("HealthPickups")
-- calling that folder
local healthPickups = healthPickupsFolder:GetChildren()
-- return array of that folder
local function onTouchHealthPickup(otherPart, healthPickup)
	if healthPickup:GetAttribute("Enabled") then
		local character = otherPart.Parent
		local humanoid = character:FindFirstChildWhichIsA("Humanoid")
		if humanoid then
			humanoid.Health = MAX_HEALTH
			healthPickup.Transparency = DISABLED_TRANSPARENCY
			healthPickup:SetAttribute("Enabled", false)
			task.wait(COOLDOWN)
			healthPickup.Transparency = ENABLED_TRANSPARENCY
			healthPickup:SetAttribute("Enabled", true)
		end
	end
end

for _, healthPickup in ipairs(healthPickups) do
	healthPickup:SetAttribute("Enabled", true)
	healthPickup.Touched:Connect(function(otherPart) -- when health is touched activate function
		onTouchHealthPickup(otherPart, healthPickup)
	end)
end