from collections import defaultdict


class Solution():
    def main(self):
        ordered = defaultdict(list)
        with open('day5/aoc05s.txt', 'r') as file:
            rules = True
            total = 0
            for line in file:
                line = line.strip()  
                if line != '':
                    if rules:
                        nums = line.split('|')
                        ordered[nums[0]].append(nums[1])
                    else:
                        pages = line.strip().split(',')
                        page_hash = set()
                        bad = False
                        for i, page in enumerate(pages):
                            for pre in ordered[page]:
                                if pre in page_hash:
                                    print(f'Page {page} breaks rule {pre}')
                                    bad = True
                                    break
                            if bad: 
                                print('Bad line: ', line)
                                break
                            page_hash.add(page)
                        if not bad:
                            total += int(pages[len(pages)//2])
                else:
                    rules = False

        print(total)

if __name__ == "__main__":
    Solution().main()