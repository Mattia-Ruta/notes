// Menu Class

namespace Menus {
    public class Menu {
        private List<String> Lines = new List<String>();
        public int AddLine(string line) {
            // Append line to Lines
            Lines.Add(line);

            return Lines.Count();
        }

        public int GetCount() {
            // Returns how many lines the menu has
            return Lines.Count();
        }
    }
}