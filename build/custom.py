# custom.py, modified from https://popcar.bearblog.dev/how-to-minify-godots-build-size/
target="template_release"
debug_symbols="no"
optimize="size_extra" # Godot >4.5 only. Otherwise, use optimize="size"
lto="full" # Much slower build times, smaller export size
production="yes"

disable_3d="yes"

deprecated="no"  # Disables deprecated features
vulkan="no"      # Disables the Vulkan driver (used in Forward+/Mobile Renderers)
use_volk="no"    # Disables more Vulkan stuff
openxr="no"      # Disables Virtual Reality/Augmented Reality stuff
minizip="no"     # Disables ZIP archive support
graphite="no"    # Disables SIL Graphite smart fonts support

module_gdscript_enabled="yes"
module_svg_enabled="yes"
module_webp_enabled="yes"
module_godot_physics_2d_enabled="no"
module_mono_enabled="yes" # disable if you don't need mono

# These next few options were introduced in Godot 4.5!
disable_navigation_2d="yes"
disable_navigation_3d="yes"
disable_xr="yes"