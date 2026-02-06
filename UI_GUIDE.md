# 🎨 UI/UX Guide - AI Assessment Platform

## Design System

### Color Palette

**Primary Gradient**
- Purple: #667eea → #764ba2
- Used for: Headers, buttons, highlights

**Status Colors**
- Success: #10b981 (Green)
- Warning: #f59e0b (Orange)
- Error: #ef4444 (Red)
- Info: #3b82f6 (Blue)

**Difficulty Badges**
- Easy: #d1fae5 (Light Green)
- Medium: #fef3c7 (Light Yellow)
- Hard: #fee2e2 (Light Red)

**Rankings**
- 1st Place: Gold gradient (#fbbf24 → #f59e0b)
- 2nd Place: Silver gradient (#d1d5db → #9ca3af)
- 3rd Place: Bronze gradient (#fca5a5 → #ef4444)

### Typography
- Font Family: System fonts (-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto')
- Headings: 700 weight
- Body: 400 weight
- Labels: 600 weight

---

## Page Layouts

### 1. Login/Register Page
```
┌─────────────────────────────────────┐
│         🎯 Platform Logo            │
├─────────────────────────────────────┤
│                                     │
│   ┌───────────────────────────┐   │
│   │  Login Form               │   │
│   │  ├─ Email Input           │   │
│   │  ├─ Password Input        │   │
│   │  └─ Login Button          │   │
│   └───────────────────────────┘   │
│                                     │
│   Don't have account? Register     │
└─────────────────────────────────────┘
```

**Features:**
- Centered card layout
- Gradient background
- Clean, minimal form
- Link to switch between login/register

---

### 2. Recruiter Dashboard
```
┌─────────────────────────────────────────────┐
│  🎯 AI Assessment Platform    [Logout]      │
├─────────────────────────────────────────────┤
│  Recruiter Dashboard       [+ Create Job]   │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────┐  ┌─────────────┐         │
│  │ Job Card 1  │  │ Job Card 2  │         │
│  │             │  │             │         │
│  │ Title       │  │ Title       │         │
│  │ Skills...   │  │ Skills...   │         │
│  │ Duration    │  │ Duration    │         │
│  │             │  │             │         │
│  │[Leaderboard]│  │[Leaderboard]│         │
│  └─────────────┘  └─────────────┘         │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Create Job Form (when clicked)      │   │
│  │ ├─ Title Input                      │   │
│  │ ├─ Description Textarea (large)     │   │
│  │ ├─ Duration Input                   │   │
│  │ ├─ Cutoff Percentage Input          │   │
│  │ └─ [Create Job] Button              │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

**Features:**
- Grid layout for job cards
- Toggle form visibility
- Badge tags for skills
- Call-to-action buttons

---

### 3. Candidate Dashboard
```
┌─────────────────────────────────────────────┐
│  🎯 AI Assessment Platform    [Logout]      │
├─────────────────────────────────────────────┤
│  Available Assessments                      │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Full Stack Developer                │   │
│  │                                     │   │
│  │ Description preview...              │   │
│  │                                     │   │
│  │ Required Skills:                    │   │
│  │ [React] [Node.js] [MongoDB]        │   │
│  │                                     │   │
│  │ ⏱️ Duration: 60 min                 │   │
│  │ 📊 Passing: 60%                     │   │
│  │ 📈 Level: Mid-level                 │   │
│  │                                     │   │
│  │      [Start Assessment]             │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Data Analyst                        │   │
│  │ ... similar layout ...              │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

**Features:**
- Card-based layout
- Skill badges
- Clear information hierarchy
- Prominent CTA button

---

### 4. Assessment Taking Interface
```
┌─────────────────────────────────────────────┐
│  🎯 AI Assessment Platform    [Logout]      │
├─────────────────────────────────────────────┤
│  Question 5 of 18              70% Complete │
│  ████████████████░░░░░░░░ Progress Bar     │
├─────────────────────────────────────────────┤
│                                             │
│  Question Navigation:                       │
│  [1][2][3][4][5✓][6][7][8]...              │
│  Green = Answered, Blue = Current          │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ [MEDIUM]            [SUBJECTIVE]    │   │
│  │                                     │   │
│  │ Question: Explain how you would     │   │
│  │ optimize a slow database query...   │   │
│  │                                     │   │
│  │ ┌─────────────────────────────┐    │   │
│  │ │ Answer Textarea             │    │   │
│  │ │                             │    │   │
│  │ │                             │    │   │
│  │ └─────────────────────────────┘    │   │
│  │                                     │   │
│  │  [← Previous]        [Next →]      │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

**For MCQ Questions:**
```
│  ┌─────────────────────────────────────┐
│  │ ○ Option A: First choice           │
│  │ ○ Option B: Second choice          │
│  │ ● Option C: Selected choice        │
│  │ ○ Option D: Fourth choice          │
│  └─────────────────────────────────────┘
```

**For Coding Questions:**
```
│  ┌─────────────────────────────────────┐
│  │ # Write your code here             │
│  │ def solution(input):               │
│  │     # Your implementation          │
│  │     pass                           │
│  │                                     │
│  └─────────────────────────────────────┘
│  [Code editor with syntax highlighting]
```

**Features:**
- Progress bar at top
- Visual question navigation
- Difficulty and type badges
- Appropriate input for each question type
- Navigation between questions
- Clear submit button on last question

---

### 5. Results Page
```
┌─────────────────────────────────────────────┐
│  🎯 AI Assessment Platform    [Logout]      │
├─────────────────────────────────────────────┤
│  Assessment Results                         │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │          85.5                       │   │
│  │      ✅ Qualified                   │   │
│  │    Percentile: 78th                │   │
│  └─────────────────────────────────────┘   │
│  [Gradient purple background, white text]  │
│                                             │
│  Section-wise Performance:                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │   45.0   │ │   25.5   │ │   15.0   │   │
│  │ MCQ Score│ │Subjective│ │  Coding  │   │
│  └──────────┘ └──────────┘ └──────────┘   │
│                                             │
│  Skill-wise Performance:                   │
│  JavaScript    ████████░░ 80%              │
│  React         ██████░░░░ 65%              │
│  Node.js       ███████░░░ 70%              │
│                                             │
│  ┌────────────────┐  ┌────────────────┐   │
│  │ ✅ Strengths   │  │ ⚠️ Weaknesses  │   │
│  │ • Good at X    │  │ • Needs work Y │   │
│  │ • Excellent Y  │  │ • Improve Z    │   │
│  └────────────────┘  └────────────────┘   │
│                                             │
│  🤖 AI Analysis:                           │
│  "Candidate shows strong understanding..." │
│                                             │
│  Recommendation: ✅ Strong Hire            │
└─────────────────────────────────────────────┘
```

**Features:**
- Large, centered total score
- Color-coded sections
- Progress bars for skills
- Side-by-side strengths/weaknesses
- AI-generated summary
- Clear recommendation

---

### 6. Leaderboard Page
```
┌─────────────────────────────────────────────┐
│  🎯 AI Assessment Platform    [Logout]      │
├─────────────────────────────────────────────┤
│  🏆 Leaderboard - Full Stack Developer     │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ Rank│Name        │Score│%   │Date   │   │
│  ├─────────────────────────────────────┤   │
│  │ 🥇 │ Alice Smith│ 95.5│98% │Jan 15 │   │
│  │ 🥈 │ Bob Jones  │ 89.0│91% │Jan 14 │   │
│  │ 🥉 │ Carol White│ 85.5│87% │Jan 15 │   │
│  │  4 │ Dave Brown │ 78.0│80% │Jan 14 │   │
│  │  5 │ Eve Davis  │ 75.5│77% │Jan 13 │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  Top Performers:                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │    🥇    │ │    🥈    │ │    🥉    │   │
│  │  Alice   │ │   Bob    │ │  Carol   │   │
│  │  95.5    │ │  89.0    │ │  85.5    │   │
│  └──────────┘ └──────────┘ └──────────┘   │
│  [Gold bg]    [Silver bg]   [Bronze bg]   │
└─────────────────────────────────────────────┘
```

**Features:**
- Medal icons for top 3
- Sortable table
- Progress bars for percentages
- Highlighted top performers section
- Color-coded ranking badges

---

## Interactive Elements

### Buttons
```css
Primary Button:
├─ Gradient purple background
├─ White text
├─ Rounded corners (8px)
├─ Hover: Lift effect + shadow
└─ Active: Slight scale down

Secondary Button:
├─ Light purple background
├─ Dark purple text
├─ Same shape as primary
└─ Hover: Darken slightly
```

### Form Inputs
```css
Input Fields:
├─ White background
├─ 2px gray border
├─ Rounded corners (8px)
├─ Focus: Purple border
└─ Padding: 12px
```

### Cards
```css
Card Component:
├─ White background
├─ Rounded corners (12px)
├─ Drop shadow
├─ 24px padding
└─ Hover: Slight lift (optional)
```

### Badges
```css
Badge:
├─ Rounded pill shape
├─ Color-coded by type
├─ Small text (14px)
├─ 4px vertical padding
└─ Inline display
```

---

## Responsive Design

### Desktop (> 768px)
- Multi-column grid layouts
- Side-by-side sections
- Full-width forms
- Large text and spacing

### Mobile (< 768px)
- Single column layout
- Stacked sections
- Full-width buttons
- Adjusted font sizes
- Condensed navigation

---

## Animation & Transitions

```css
Standard Transitions:
- Button hover: 0.3s ease
- Card hover: 0.3s ease
- Border color: 0.3s ease
- Transform: 0.3s ease

Animations:
- Progress bar fill: Smooth width transition
- Page load: Fade in
- Timer warning: Pulse animation
- Success/Error: Slide in from top
```

---

## Accessibility

- ✅ High contrast ratios
- ✅ Clear focus indicators
- ✅ Keyboard navigation support
- ✅ Semantic HTML
- ✅ ARIA labels where needed
- ✅ Readable font sizes (16px minimum)

---

## User Experience Features

### Feedback
- Loading states on buttons
- Success/error messages
- Progress indicators
- Confirmation dialogs

### Navigation
- Clear breadcrumbs
- Consistent header
- Intuitive menu
- Back buttons where needed

### Data Display
- Clear hierarchy
- Visual grouping
- Color-coded information
- Icons for quick recognition

---

## Best Practices Used

1. **Consistency** - Same patterns throughout
2. **Clarity** - Clear labels and instructions
3. **Efficiency** - Minimal clicks to complete tasks
4. **Feedback** - Always inform user of system state
5. **Simplicity** - Clean, uncluttered interface
6. **Modern** - Contemporary design trends
7. **Responsive** - Works on all devices

---

This design system ensures a professional, cohesive, and user-friendly interface throughout the platform. All colors, spacing, and interactions follow consistent patterns for a polished user experience.
