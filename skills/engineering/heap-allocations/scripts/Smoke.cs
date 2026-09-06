using System;

public static class Smoke
{
    public static Func<int> Capturing(int value) => () => value;
    public static Func<int> NonCapturing() => static () => 1;
    public static object Boxing(int value) => value;
    public static int NoAllocation(int value) => value + 1;
}
