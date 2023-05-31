local pasta = true
local tomatoSauce = true

if pasta == true and tomatoSauce == true then
	print("We have spaghetti dinner")
else
	print("Something is missing...")
end
-- Output: We have spaghetti dinner

local pasta = false
local tomatoSauce = true
local garlicBread = true

if (pasta == true and tomatoSauce == true) or garlicBread == true then
	print("We have either spaghetti dinner OR garlic bread")
else
	print("Something is missing...")
end

-- Output: We have either spaghetti dinner OR garlic bread