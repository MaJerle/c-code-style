"""

Aligns inline comments that start with /* and end with */ to 12*4 spaces or to next 4-spaces alignmed if line is longer


"""
import os
import glob

# Scan all repositories in given path
# Set inc_submodules = 1 to make recursive scan
# Set libs = 1 to scan libs directory
def scan(path):
	files = []

	files = glob.glob(path, recursive = True)

	return files

# Analyse file and modify content if necessary
def align_comments(path):
	comment_start_position = 12 * 4

	# Print text
	print ("Analyzing file: " + path)

	# Open file for read and read all lines
	f = open(path, "r")
	lines = f.readlines()

	# Output content
	out_content = ""

	# Analyse line by line
	for l in lines:
		# Try to find both, opening and closing inline comment in single line
		index_open = l.find('/*')
		index_close = l.find('*/')

		"""
		Rule to select comment is
		 - Opening and closing bracket must be in the same line, so "/*" and "*/"
		 - Line must not start with "#endif" or "else", can be whatever, just not beginning
		 - Other characters than only spaces must be infront of comment
		 - Closing bracket must be last thing in line
		"""
		if index_open <= 0 or index_close <= 0 or l.find("#endif") == 0 or l.find("#else") == 0:
			out_content = out_content + l
			continue

		# Check characters before opening bracket
		can_continue = False;
		for i in range(0, index_open):
			if l[i] != ' ' and l[i] != '\t':
				can_continue = True
				break;
		if not can_continue:
			out_content = out_content + l
			continue;

		# Check if closing bracket is last thing in the line
		index_close = index_close + 2 	# Go to the end of closing comment section "*/"
		l_len = len(l)					# Get line length
		if not (index_close == l_len - 2 and l[-2] == '\r' and l[-1] == '\n') and not (index_close == l_len - 1 and (l[-1] == '\r' or l[-1] == '\n')):
			out_content = out_content + l
			continue;

		# Check if something has to be done with the comment itself
		if index_open == comment_start_position:
			out_content = out_content + l
			continue;

		# First remove all spaces between end of code and comment itself
		tmp_l = l[0:index_open]
		while tmp_l[-1] == ' ':
			tmp_l = tmp_l[:-1]

		# Add spaces to match up to wished len
		while len(tmp_l) < comment_start_position or len(tmp_l) % 4 != 0:
			tmp_l = tmp_l + " "

		# Now add comment part
		final_l = tmp_l + l[index_open:]

		# Add new line to output content
		out_content = out_content + final_l

	# Now open file again and write content
	f = open(path, "w")
	f.truncate()
	f.write(out_content)
	f.close()

	return True

# Get base path
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get all C and H files for all projects
files = []
files = files + scan(base_path + "/lwesp/lwesp/**/*.c") + scan(base_path + "/lwesp/lwesp/**/*.h")
files = files + scan(base_path + "/lwgps/lwgps/**/*.c") + scan(base_path + "/lwgps/lwgps/**/*.h")
files = files + scan(base_path + "/lwgsm/lwgsm/**/*.c") + scan(base_path + "/lwgsm/lwgsm/**/*.h")
files = files + scan(base_path + "/lwmem/lwmem/**/*.c") + scan(base_path + "/lwmem/lwmem/**/*.h")
files = files + scan(base_path + "/lwow/lwow/**/*.c") + scan(base_path + "/lwow/lwow/**/*.h")
files = files + scan(base_path + "/lwpkt/lwpkt/**/*.c") + scan(base_path + "/lwpkt/lwpkt/**/*.h")
files = files + scan(base_path + "/lwprintf/lwprintf/**/*.c") + scan(base_path + "/lwprintf/lwprintf/**/*.h")
files = files + scan(base_path + "/lwrb/lwrb/**/*.c") + scan(base_path + "/lwrb/lwrb/**/*.h")

# Analyse all files
for f in files:
	if f.find('third_party') != -1:
		continue
	align_comments(f)