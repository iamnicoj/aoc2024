from collections import defaultdict, deque

class Solution():
    def read_rules(self, file, ordered):
        # Read all rules until a blank line
        for line in file:
            line = line.strip()
            if line == '':
                # Blank line: no more rules
                break
            X, Y = line.split('|')
            ordered[X].append(Y)

    def process_update(self, pages, ordered):
        page_hash = {p: i for i, p in enumerate(pages)}
        bad = False
        graph = defaultdict(list)
        indegree = [0]*len(pages)
        
        # Build graph and check order
        for X in ordered:
            for Y in ordered[X]:
                if X in page_hash and Y in page_hash:
                    if page_hash[X] > page_hash[Y]:
                        bad = True
                    graph[X].append(Y)
                    indegree[page_hash[Y]] += 1

        # If bad, fix order with topological sort and return mid page
        if bad:
            return self.topological_sort_and_get_mid(pages, graph, indegree, page_hash)
        
        # If not bad, return None to indicate no addition to total
        return None

    def topological_sort_and_get_mid(self, pages, graph, indegree, page_hash):
        zero_indegree = deque([p for p in pages if indegree[page_hash[p]] == 0])
        sorted_order = []

        while zero_indegree:
            node = zero_indegree.popleft()
            sorted_order.append(node)
            for succ in graph[node]:
                indegree[page_hash[succ]] -= 1
                if indegree[page_hash[succ]] == 0:
                    # THE MOST IMPORTANT LINE IN THIS PROBLEM THAT IS NOT MENTIONED IN THE DESCRIPTION. 
                    # YOU NEED TO ADD THE ZERO DEGREE PAGES TO THE LEFT OF THE QUEUE
                    zero_indegree.appendleft(succ) 

        mid_page = sorted_order[len(sorted_order)//2]
        return int(mid_page)

    def main(self):
        ordered = defaultdict(list)
        total = 0

        with open('day5/aoc05s.txt', 'r') as file:
            self.read_rules(file, ordered)
            
            # Now read updates
            for line in file:
                line = line.strip()
                if line == '':
                    continue
                pages = line.split(',')
                mid_page_val = self.process_update(pages, ordered)
                if mid_page_val is not None:
                    total += mid_page_val

        print(total)

if __name__ == "__main__":
    Solution().main()