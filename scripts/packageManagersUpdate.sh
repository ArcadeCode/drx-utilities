corepack prepare npm@latest --activate
corepack prepare pnpm@latest --activate
corepack prepare yarn@latest --activate
echo echo "Last version of npm installed : $(npm --version)"
echo echo "Last version of pnpm installed : $(pnpm --version)"
echo echo "Last version of yarn installed : $(yarn --version)"
sleep 5